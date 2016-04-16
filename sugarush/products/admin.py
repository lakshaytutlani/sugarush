from django.contrib import admin
from .models import Products,Shops

# Register your models here.
#admin.site.register(Products)
#admin.site.register(Shops)

@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'shop_area', 'shop_pincode','shop_image']
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'shop','price','image']
   
