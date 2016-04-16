from django.conf.urls import url
from .views import login,logout,forgot,reset_password,signup,sign_up,updatesignup


urlpatterns = [
     url(r'^login/$',login,name="login"),
     url(r'^logout/$',logout,name="logout"),
     url(r'^forgot/$',forgot,name="forgot"),
     url(r'^reset/(?P<id>\d+)/(?P<otp>\d{4})/$', reset_password, name="reset_password"),
     url(r'^sign_up/$',sign_up, name ="sign_up" ),
     url(r'^signup/(?P<id>\d+)/(?P<otp>\d{4})/$', signup, name="signup"),
     url(r'^updatesignup/$',updatesignup,name = "updatesignup")
  
]

