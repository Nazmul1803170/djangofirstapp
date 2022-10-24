from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path("signup", signupview, name = "signup"),
    path("login", loginView, name = "login"),
    path("logout", logoutView, name = "logout"),
    path("product", product, name = "product"),
    path("dashboard/<int:pk>", dashboardView, name = "dashboard"),
    path("dataset/<int:pk>", datasetView, name = "dataset"),
]