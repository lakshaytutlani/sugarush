from django.db import models

# Create your models here.


class Shops(models.Model):
  shop_name = models.CharField(max_length=255,blank=False,null=False)
  shop_area =  models.CharField(max_length=255,blank=False,null=False,default='unknown')
  shop_pincode = models.IntegerField(blank=False,null=False,default=110001)
  shop_address =  models.CharField(max_length=255,blank=False,null=False)
  shop_image = models.ImageField(upload_to = 'shop_pic_folder/')
  
  def __str__(self):
        return '%s' % (self.shop_name)


class Products(models.Model):
 
 TYPE_PURPOSE_CHOICES = (
        ('SWEET', 'sweet'),
        ('SNACK', 'snack'),
    );

 TYPE_QTY_CHOICES = (
        ('/plate', '/ plate'),
        ('/1000g', '/ 1000g'),
    );
 
 name = models.CharField(max_length=255,blank=False,null=False)
 shop = models.ForeignKey(Shops,related_name='manufacturer')
 price = models.IntegerField(blank=False,null=False)
 description = models.TextField()
 quantity = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False)
 type = models.CharField(max_length = 5, choices = TYPE_PURPOSE_CHOICES)
 qty_type = models.CharField(max_length = 6, choices = TYPE_QTY_CHOICES,default='/plate')
 image = models.ImageField(upload_to = 'product_pic_folder/')

 def __str__(self):
        return '%s (%s)' % (self.name,self.shop)

