import json
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.shortcuts import render
from .models import Category,Product,OrderItem,Order
from .place import provinces,cities
# Create your views here.

def products(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    
    context={'categorys':categorys,'products':products}
    return render(request,'products/products.html',context)


def product(request,pk):
    product = Product.objects.get(id=pk)
    
    context={'product':product}
    return render(request,'products/product.html',context)

def addCart(request):
    data = json.loads(request.body)
    print(data)
    productId = data['productId']
    action = data['action']

    user = request.user
    product = Product.objects.get(id = productId)
    # dd pag kuwa order na ini na product na false an
    #complete pag diri existing pag himu nala cton
    #instance
    order,created = Order.objects.get_or_create(customer=user,complete=False)

    #same dd ta
    orderItem,created = OrderItem.objects.get_or_create(product=product,order=order)
   
    if(action == "add"):
        orderItem.quantity=orderItem.quantity+1 # type: ignore
    orderItem.save()
    messages.success(request,'added to cart')
# Serialize the order item to a dictionary
    order_item_data = serializers.serialize('python', [orderItem])[0]['fields']

# Return the serialized order item data as JSON response
    return JsonResponse({'orderItem': order_item_data},safe=False)

def showCart(request):
    user = request.user
    try:
        order = Order.objects.get(customer =user,complete=False)
        orderItem = order.orderitem_set.all() # type: ignore
        context = {'orderItem':orderItem,'total':order.get_cart_total}
    except Order.DoesNotExist:
        context={}
        
    return render(request,'products/cart.html',context)

def address(request):
    user = request.user
    mun =cities("0848")
 
    try:
        order = Order.objects.get(customer =user,complete=False)
        orderItem = order.orderitem_set.all() # type: ignore
        context = {'orderItem':orderItem,'total':order.get_cart_total,'mun':mun}
    except Order.DoesNotExist:
        context ={'mun':mun}
    
    
    return render(request, 'products/address.html',context)