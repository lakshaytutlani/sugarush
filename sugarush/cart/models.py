from django.db import models
from accounts.models import MyUser
from products.models import Shops,Products



# Create your models here.
class Order(models.Model):
 DEFAULT_STATUS_ID = 1 	
 customer=models.ForeignKey(MyUser,related_name='customer')
 status_code = models.ForeignKey('StatusCode',default=DEFAULT_STATUS_ID)
 date_placed = models.DateTimeField(auto_now_add=True)
 total_price = models.DecimalField(max_digits=7, decimal_places=2)
 def __str__(self):
        return '%s' % (self.id)



class StatusCode(models.Model):
 ORDER_PURPOSE_CHOICES = (
        ('BOOKED', 'Order Booked'),
        ('DELIVER', 'Order Delivered'),
	('CANCELLED','Order Cancelled')
    );

 short_name = models.CharField(max_length=10,choices = ORDER_PURPOSE_CHOICES,default='BOOKED')
 name = models.CharField(max_length=300)
 description = models.TextField()

 def __str__(self):
        return '%s' % (self.short_name)

	

class ProductInOrder(models.Model):
 
 order = models.ForeignKey(Order)
 product = models.ForeignKey(Products)
 unit_price =  models.IntegerField(blank=False,null=False)
 total_price = models.DecimalField(max_digits=7, decimal_places=2)
 quantity = models.PositiveIntegerField()
	
 def __str__(self):
        return '%s%s' % (self.order,self.product)
 

