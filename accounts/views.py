from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
import requests
import json

# Create your views here.

def loginView(req):
    data = ""
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(req,user)
        print(user)

        try:
            userinfo = UserInfo.objects.get(user=user)
        except:
            userinfo = None
        
        return redirect('home')

    return  render(req, 'home.html')

def signupview(req):
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            name = req.POST.get('name')
            contact = req.POST.get('contact')
            email = req.POST.get('email')
            username = req.POST.get('username')
            password = req.POST.get('password1')
            
            form.save()
            user = authenticate(username=username, password=password)
            userinfo = UserInfo.objects.create(user=user)
            login(req, user)
            userinfo.name = name
            userinfo.contact = contact
            userinfo.email = email
            userinfo.product_id = None
            userinfo.save()

            return redirect('login')
    else:
        form = SignupForm()

    return render(req, 'signup.html', {'form': form})

def dashboardView(req,pk):

    userinfo = UserInfo.objects.get(pk=pk)
    if userinfo.user == req.user:
        product_id = userinfo.product_id

        api_link = 'https://shantotech003.000webhostapp.com/esp_data_json_api.php?product_id=' + product_id
        api_request = requests.get(api_link)
        my_json = api_request.content.decode('utf8').replace("'", '"')
        data = json.loads(my_json)

        return render(req,'dashboard.html', {'data':data, 'user':userinfo})

    else:
        return redirect('home')

def logoutView(req):
    logout(req)
    return redirect('home')

def product(req):
    return render(req, 'basic.html')