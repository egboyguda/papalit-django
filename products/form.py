from django.forms import ModelForm
from django import forms
from .models import ShippingAddress

class ShippingForm(ModelForm):
    class Meta:
        model=ShippingAddress
        fields= ['mun','address']
    