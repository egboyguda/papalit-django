import json
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import Category,Product,OrderItem,Order
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
        orderItem.quantity=orderItem.quantity+1
    orderItem.save()
# Serialize the order item to a dictionary
    order_item_data = serializers.serialize('python', [orderItem])[0]['fields']

# Return the serialized order item data as JSON response
    return JsonResponse({'orderItem': order_item_data},safe=False)