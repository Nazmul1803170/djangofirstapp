from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductInfo(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=50, default='ShantoTech Ltd')
    product_code = models.CharField(max_length=20)
    sold =models.BooleanField(default=False)

    def __str__(self):
        return  self.product_id

class OrderInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null= True)
    product_id = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    
    payment = models.CharField(max_length=20)
    order_receive = models.BooleanField(default=False)
    order_delevary = models.BooleanField(default=False)
    order_delevered = models.BooleanField(default=False)

    def __str__(self):
        return  self.product_id

