import uuid
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length = 200,null =True,blank = True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name= models.CharField(max_length =200, null=True,blank =True)
    price = models.DecimalField(null = True,blank =True,decimal_places=2,max_digits=6)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE,null=True,blank =True)
    image= models.ImageField(null=True,blank=True,default='default.jpg')
    is_sale =models.BooleanField(default=False)
    sale_price =models.DecimalField(null = True,blank =True,decimal_places=2,max_digits=6)
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
