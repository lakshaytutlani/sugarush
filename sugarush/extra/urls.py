from django.conf.urls import url,include
from django.contrib import admin
from .views import contactus,whatwedo


urlpatterns=[
        url(r'^contactus/$', contactus,name="contactus"),
        url(r'^whatwedo/$',whatwedo,name="whatwedo"),
]


