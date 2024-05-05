import uuid
from django.db import models

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
    
