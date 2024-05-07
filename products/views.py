import json
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
    productId = data['productId']
    action = data['action']

    user = request.user
    product = Product.objects.get(id = productId)
    order,created = Order.objects.get_or_create(customer=user,complet=False)

    orderItem = OrderItem.objects.get_or_create(product=product,customer=user)
    if(action == "add"):
        orderItem.quantity=+1
    pass