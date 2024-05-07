from django.shortcuts import render
from .models import Category,Product
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