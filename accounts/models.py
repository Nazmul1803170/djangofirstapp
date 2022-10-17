from itertools import product
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null= True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    product_id = models.CharField(max_length=20, null= True ,blank=True,)
    device_linked = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return  self.name
