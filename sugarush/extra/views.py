from django.shortcuts import render
from django.http import HttpResponse
from products.models import Shops


# Create your views here.

def whatwedo(request):
 return render(request,'extra/whatwedo.html',{'shop_list' : Shops.objects.all().order_by('shop_name')})

def contactus(request): 
 return render(request,'extra/contactus.html',{'shop_list' : Shops.objects.all().order_by('shop_name')})
