from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products,Shops
from .models import ProductInOrder,StatusCode,Order
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.mail import send_mail
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from datetime import datetime
from accounts.models import MyUser
from django.core.mail import EmailMessage
from io import BytesIO

# Create your views here.

def add_to_cart(request):
 if not request.user.is_authenticated():
    return HttpResponse("Please Login First")		

 
 if request.is_ajax():
    print('execute')

    ourid = request.GET.get('id','')
    length=0
    if ourid == 'initial':
     ordercheck=Order.objects.filter(customer=request.user,status_code='1')
     if len(ordercheck) != 0:
      y=ProductInOrder.objects.filter(order=ordercheck[0])
      length=len(y)
     return HttpResponse(" ,"+str(length))


    info=Products.objects.filter(id=ourid)	    
    
    print (info[0].name +"  "+str(info[0].shop)+" "+str(info[0].price))
    ordercheck=Order.objects.filter(customer=request.user,status_code='1')
    
    if len(ordercheck) != 0:
     print("order exixts")
     x=ProductInOrder.objects.filter(order=ordercheck[0],product=info[0])
     if(len(x) != 0):
      y=ProductInOrder.objects.filter(order=ordercheck[0]) 
      return HttpResponse('Already present in Cart '+str(request.user)+','+str(len(y))) 
     else:
      s=ProductInOrder.objects.create(order=ordercheck[0],product=info[0],unit_price=info[0].price,quantity=1,total_price=1*info[0].price)
      y=ProductInOrder.objects.filter(order=ordercheck[0])
      return HttpResponse(ourid+" "+str(info[0].name)+" added to cart ,"+str(len(y)))

			
    else:	
     q=Order.objects.create(customer=request.user,total_price=0)	
     print(q)
     #x=1*info[0]*unit_price
     s=ProductInOrder.objects.create(order=q,product=info[0],unit_price=info[0].price,quantity=1,total_price=1*info[0].price)
     y=ProductInOrder.objects.filter(order=q.id)
     return HttpResponse(ourid+" "+str(info[0].name)+" added to cart ,"+str(len(y)))
 return HttpResponse('hi')


def cart(request):
 if request.user.is_authenticated():
  ordercheck=Order.objects.filter(customer=request.user,status_code='1')
  if(len(ordercheck) == 0):
   return render(request,'cart/emptycart.html')
  x=ProductInOrder.objects.filter(order=ordercheck[0])
  context={'id':ordercheck[0].id,'order_list': x ,'shop_list' : Shops.objects.all().order_by('shop_name'),'prod_list' : Products.objects.all().order_by('name')} 
  return render(request,'cart/cart.html',context)	


def deleteitem(request,order_id=None,product_id=None):
  if request.user.is_authenticated():
   ProductInOrder.objects.filter(order_id=order_id,product_id=product_id).delete()
  return redirect("cart")


def cartupdate(request,order_id=None):
 if request.user.is_authenticated():
  
  if request.is_ajax():
    print('update')
    value=0;
    total = request.GET.getlist('totalprice[]');
    qty = request.GET.getlist('quant[]');
    for x in total:
     print(x) 
    #for y in qty:
    # print(y)
    i=0
    t=ProductInOrder.objects.filter(order_id=order_id)
    print(len(t)) 
    for b in t:
     print(i)
     b.quantity=qty[i]
     print(i)
     b.total_price=total[i]
     value=value+int(total[i])   
     b.save(); 
     i=i+1
   
    a=Order.objects.get(id=order_id)
    a.total_price=value
    a.save();
 return redirect("cart")

def checkout(request,order_id=None):
 if request.user.is_authenticated():
       
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="order.pdf"'
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.setLineWidth(.3) 
    p.setFont('Helvetica', 12)
 
    p.drawString(30,750,'SUGARUSH')
    p.drawString(30,735,'ORDER BOOKED')
    ordercheck=Order.objects.filter(id=order_id)
    x=ProductInOrder.objects.filter(order=ordercheck[0])
    
    p.drawString(400,750,str(ordercheck[0].date_placed))
    p.line(480,747,580,747)
 
    p.drawString(275,725,'AMOUNT GENERATED:')
    p.drawString(500,725,str(ordercheck[0].total_price))
    p.line(378,723,580,723)
 
    p.drawString(30,703,'ITEMS PURCHASED')
    p.drawString(200,703,'UNIT COST')
    p.drawString(300,703,'QTY')
    p.drawString(400,703,'TOTAL AMT')
    

    val=680
    for y in x:
     product=Products.objects.get(id=y.product_id)
     p.drawString(60,val,product.name)
     p.drawString(200,val,str(y.unit_price))
     p.drawString(300,val,str(y.quantity))
     p.drawString(400,val,str(y.total_price))
     val=val-20
    
    user=MyUser.objects.get(id=request.user.id)
    p.drawString(50,470,"USER:")
    p.drawString(200,470,user.first_name+user.last_name)
    p.drawString(50,450,"ADDRESS FOR DELIVERY:")
    p.drawString(200,430,user.deliveryaddress)
    p.drawString(200,410,user.landmark+"  "+user.pincode)
    p.drawString(100,350,"ORDER WILL BE DELIVERD WITH IN 45 MINUTES")  
    p.drawString(150,300,'Thank You For Purchase :)')
    p.showPage()
    p.save()
    

    message = EmailMessage('Sugarush Order Confirm', 'Order confirmed and will be deliverd in 45 minutes', 'lakshaytutlani@gmail.com',
    [user.email], ['lakshaytutlani@gmail.com'],
    headers = {'Reply-To': 'another@example.com'})
    #attachment = open('order.pdf', 'rb')
    pdf = buffer.getvalue()
    buffer.close()
    message.attach('order.pdf',pdf,'application/pdf')
    message.send()

    a=Order.objects.get(id=order_id)
    a.status_code_id=2
    a.save();


    
      
    return redirect('cart')
    #send_mail('sugarush password reset.', 'your link is : %s' % (link), 'laksha$
    #[user.email])
 
def order(request):
 if request.user.is_authenticated():
  status=StatusCode.objects.all(); 
  context={'shop_list' : Shops.objects.all().order_by('shop_name'),'order':Order.objects.filter(customer_id=request.user.id,status_code_id=2),'status':status}
  
 return render(request,'cart/order.html',context)
     
def detailorder(request,order_id=None):
 if request.user.is_authenticated():
  product=Products.objects.all()
  shop=Shops.objects.all()
  context={'shop':shop,'product':product,'allproducts':ProductInOrder.objects.filter(order_id=order_id),'shop_list' : Shops.objects.all().order_by('shop_name')}
 return render(request,'cart/detailorder.html',context) 
