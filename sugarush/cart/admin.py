from django.contrib import admin
from .models import Order,ProductInOrder,StatusCode


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =  ['customer','id','total_price']

@admin.register(StatusCode)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']

@admin.register(ProductInOrder)
class PlacedAdmin(admin.ModelAdmin):
    list_display = ['order', 'product','unit_price','quantity']



