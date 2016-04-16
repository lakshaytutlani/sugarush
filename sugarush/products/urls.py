from django.conf.urls import url,include
from .views import all_products,all_snacks,all_sweets,show_shop,searchproduct,oneproduct,sortedProduct


urlpatterns = [
     url(r'^all/$', all_products,name="allproducts"),
     url(r'^snacks/$',all_snacks,name = "allsnacks"),
     url(r'^sweets/$',all_sweets,name = "allsweets"),
     url(r'^shops/(?P<id>\d+)/$',show_shop,name="shopshow"),
     url(r'^searchproduct/$',searchproduct,name="searchproduct"),
     url(r'^oneproduct/(?P<id>\d+)/$',oneproduct,name="oneproduct"),
     url(r'^sortedproduct/(?P<id>\d+)/$',sortedProduct,name="sortedProduct")

]

