from django.shortcuts import render,redirect,get_object_or_404
from .models import MyUser,create_otp,get_valid_otp_object
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from .forms import LoginForm,ForgotForm,RefillForm,SignUpForm,UpdateSignUpForm
from django.core.mail import send_mail
from datetime import datetime
from products.models import Shops,Products

# Create your views here.

@require_http_methods(['GET', 'POST'])
def login(request):
  
  if request.user.is_authenticated():
   return redirect(reverse('index'));
  if request.method == 'GET':
   context = { 'f' : LoginForm(),'shop_list' : Shops.objects.all()};
   return render(request, 'accounts/auth/login.html', context);
  else:
   f = LoginForm(request.POST)
  if not f.is_valid():
   return render(request, 'accounts/auth/login.html', {'f' : f,'shop_list' : Shops.objects.all()});
  else:
   user = f.authenticated_user
   auth_login(request, user)
   return redirect(reverse('index'));

def logout(request):
 auth_logout(request)
 return redirect(reverse('index'))


@require_http_methods(['GET', 'POST'])
def forgot(request):
  if request.user.is_authenticated():
   return redirect(reverse('index'));
  if request.method == 'GET':
   context = { 'f' : ForgotForm(),'shop_list' : Shops.objects.all()};
   return render(request, 'accounts/auth/forgot.html', context);
  else:
   f = ForgotForm(request.POST)
   if not f.is_valid():
    return render(request, 'accounts/auth/forgot.html', {'f' : f,'shop_list' : Shops.objects.all()});
   else:
    user = MyUser.objects.get(username = f.cleaned_data['username'])
    otp = create_otp(user = user, purpose = 'FP')
    link='http://127.0.0.1:8000/accounts/reset/%s/%s' % (user.id,otp)

    send_mail('sugarush password reset.', 'your link is : %s' % (link), 'lakshaytutlani@gmail.com',
    [user.email])
    return render(request, 'accounts/auth/reset.html', {'u': user,'shop_list' : Shops.objects.all()})

@require_http_methods(['GET', 'POST'])
def reset_password(request,id = None, otp = None):
    if request.user.is_authenticated():
        return redirect(reverse('index'));
    user = get_object_or_404(MyUser, id=id);
    otp_object = get_valid_otp_object(user = user, purpose='FP', otp = otp)
    if not otp_object:
        raise Http404();
    if request.method == 'GET':
        context = { 'f' : RefillForm(), 'otp': otp_object.otp, 'uid': user.id,'shop_list' : Shops.objects.all()};
        return render(request, 'accounts/auth/refill.html', context);
    else:
        f = RefillForm(request.POST)
        if not f.is_valid():
         context = { 'f' : f, 'otp': otp_object.otp, 'uid': user.id}
         return render(request, 'accounts/auth/refill.html', context)
        else:
         user.set_password(f.cleaned_data['new_password'])
         user.save()
         otp_object.delete()
         return render(request, 'accounts/auth/set_password_success.html', { 'u' : user,'shop_list' : Shops.objects.all()})

@require_http_methods(['GET', 'POST'])
def sign_up(request):
   if request.user.is_authenticated():
    return redirect(reverse('index'));
   if request.method == 'GET':
     context = { 'f' : SignUpForm(),'shop_list' : Shops.objects.all()};
     return render(request, 'accounts/auth/signup.html', context);
   else:
     f = SignUpForm(request.POST)
     if not f.is_valid():
      return render(request, 'accounts/auth/signup.html', {'f' : f,'shop_list' : Shops.objects.all()});
     user = MyUser.objects.create(username = f.cleaned_data['username'],first_name = f.cleaned_data['firstname'],last_name = f.cleaned_data['lastname'],
email = f.cleaned_data['email'],phone = f.cleaned_data['phone'],password = f.cleaned_data['new_password'],date_joined = datetime.now(),is_active = 0)
     user.set_password(f.cleaned_data['new_password'])
     user.save()
     otp = create_otp(user = user, purpose = 'AA')
     link='http://127.0.0.1:8000/accounts/signup/%s/%s' % (user.id,otp)
     send_mail('sugarush signup link.', 'your link is : %s' % (link), 'lakshaytutlani@gmail.com',[user.email])
     return render(request, 'accounts/auth/signupconfirm.html', {'u': user,'shop_list' : Shops.objects.all()})

def signup(request,id = None,otp = None):
 if request.user.is_authenticated():
        return redirect(reverse('index'));
 user = get_object_or_404(MyUser, id=id);
 otp_object = get_valid_otp_object(user = user, purpose='AA', otp = otp)
 if not otp_object:
   raise Http404();
 else:
  user.is_active = '1'
  user.save()
  otp_object.delete()
  return render(request, 'accounts/auth/signinconfirm.html', {'u': user,'shop_list' : Shops.objects.all()})

@require_http_methods(['GET', 'POST'])
def updatesignup(request):
 user = MyUser.objects.get(id = request.user.id)
 if request.method == 'GET':
  #user = MyUser.objects.get(id = request.user.id)
  form = UpdateSignUpForm(instance = user)
  return render(request,'accounts/auth/updatesignup.html',{'f' : form,'shop_list' : Shops.objects.all()})
 else:
  form = UpdateSignUpForm(request.POST,instance = user)
  if not form.is_valid():
    return render(request, 'accounts/auth/updatesignup.html', {'f' : form,'shop_list' : Shops.objects.all()});
  form.save()
  return redirect(reverse('index'))


