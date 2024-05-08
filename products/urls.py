from django.urls import path
from . import views

urlpatterns = [
    path('',views.products,name='products'),
    path('product/<str:pk>',views.product, name='product'),
    path('addcart/',views.addCart,name='addCart')
]
