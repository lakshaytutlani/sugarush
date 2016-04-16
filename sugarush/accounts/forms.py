from django import forms
from .models import MyUser
from django.contrib.auth import authenticate
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Enter Username',max_length = 25,
help_text=' (25 characters max.)');
    password = forms.CharField(label='Enter Password',widget = forms.PasswordInput)
    error_css_class = 'error'
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        self.authenticated_user = None;
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        if MyUser.objects.filter(username = username).count() != 1:
            raise forms.ValidationError('Invalid Username')
        if MyUser.objects.filter(username = username ,is_active = '0').exists():
            raise forms.ValidationError('Please Activate your account first')
        return username

    def clean(self):
        username = self.cleaned_data.get('username', '')
        passwd = self.cleaned_data.get('password', '')
        user=authenticate(username=username, password=passwd)
        if username and passwd and not user:
            raise forms.ValidationError('Username/Password doesnot match')
        self.authenticated_user=user
        return self.cleaned_data;

class ForgotForm(forms.Form):
   username = forms.CharField(label='Enter Username',max_length = 25,
help_text=' (25 characters max.)');
   error_css_class = 'error'
   required_css_class = 'required'

   def clean_username(self):
    username=self.cleaned_data.get('username','')
    if username and not MyUser.objects.filter(username = username).exists():
       raise forms.ValidationError('Invalid Username')
    return username;

class RefillForm(forms.Form):
 new_password = forms.CharField(widget=forms.PasswordInput)
 confirm_password = forms.CharField(widget=forms.PasswordInput)
 error_css_class = 'error'
 required_css_class = 'required'
 
 def clean_confirm_password(self):
        data_new_password = self.cleaned_data.get('new_password')
        data_confirm_password = self.cleaned_data.get('confirm_password')
        if (data_new_password and data_confirm_password
                and data_new_password != data_confirm_password):
            raise forms.ValidationError("The two passwords field didn't match")
        return data_confirm_password

class SignUpForm(forms.Form):
  username = forms.CharField(label='Enter Username:',max_length = 25,
help_text=' (25 characters max.)');
  firstname = forms.CharField(label="Enter First Name:",max_length=25)
  lastname = forms.CharField(label="Enter Last Name:",max_length=25)
  phone = forms.CharField(label="Enter Contact No:",max_length=25)
  email = forms.EmailField(label="Enter Email Id:",max_length=100)
  new_password = forms.CharField(widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput)
  error_css_class = 'error'
  required_css_class = 'required'
  
  def clean_username(self):
    username=self.cleaned_data.get('username','')
    if username and MyUser.objects.filter(username = username).exists():
       raise forms.ValidationError('Username exists')
    return username;

  def clean_email(self):
    email=self.cleaned_data.get('email','')
    if email and MyUser.objects.filter(email = email).exists():
       raise forms.ValidationError('email id already registerd for other user.')
    return email;

  def clean_confirm_password(self):
        data_new_password = self.cleaned_data.get('new_password')
        data_confirm_password = self.cleaned_data.get('confirm_password')
        if (data_new_password and data_confirm_password
                and data_new_password != data_confirm_password):
            raise forms.ValidationError("The two passwords field didn't match")
        return data_confirm_password

class UpdateSignUpForm(ModelForm):
   #password = forms.CharField(max_length=20, widget=forms.PasswordInput)
   #confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput)
   error_css_class = 'error'
   required_css_class = 'required'
   
   def clean_username(self):
    data_username=self.cleaned_data.get('username','')
    user=MyUser.objects.filter(username = data_username)
    if data_username and user.exists() and data_username == user[0].username:
       return data_username
    elif data_username and user.exists():
       raise forms.ValidationError('Username exists')
    return data_username;

   def clean_email(self):
        data_email = self.cleaned_data.get('email', '')
        data_username=self.cleaned_data.get('username','')
        email=MyUser.objects.filter(email = data_email)
        if not data_email:
            raise forms.ValidationError('This field is required')
        if email.exists() and email[0].username == data_username and email[0].email == data_email:
            return data_email
        elif data_email and email.exists():
            raise forms.ValidationError('User with this email already exist')
        return data_email
   class Meta:
     model = MyUser
     fields = ['username','first_name', 'last_name', 'phone','email','deliveryaddress','landmark','pincode']

