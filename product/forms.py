import imp
from xml.etree.ElementInclude import include
from django.contrib.auth.models import User
from django.contrib.auth import forms
from django import forms
from .models import *

class OrderForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    payment_method = (
        ('Cash on Delivary','Cash on Delivary'),
        ('bKash','bKash'),
        ('Rocket','Rocket'),
        ('Visa Card','Visa Card'),
    )


class AddProductForm(forms.Form):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    product_id = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    price= forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    manufacturer = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    product_code = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    
    