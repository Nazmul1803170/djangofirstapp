from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("getstart", getstart, name = "getstart"),
    path("productlist", productlist, name = "productlist"),
    path("addproduct", addproduct, name = "addproduct"),
    path("orderproduct/<int:pk>", orderproduct, name = "orderproduct"),
    path("userprofile/<int:pk>", userprofile, name = "userprofile"),
]