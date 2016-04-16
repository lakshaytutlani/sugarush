from django.conf.urls import url,include
from django.contrib import admin
from .views import add_to_cart,cart,deleteitem,cartupdate,checkout,order,detailorder


urlpatterns=[
	url(r'^addtocart/$', add_to_cart,name="addtocart"),
	url(r'^cart/$',cart,name="cart"),
        url(r'^cartupdate/(?P<order_id>\d+)/$',cartupdate,name="cartupdate"), 
        url(r'^deleteitem/(?P<order_id>\d+)/(?P<product_id>\d+)/$',deleteitem,name="deleteitem"),
        url(r'^checkout/(?P<order_id>\d+)/$',checkout,name="checkout"),
        url(r'^order/$',order,name="order"),
        url(r'^detailorder/(?P<order_id>\d+)/$',detailorder,name="detailorder") 
           
 
]
