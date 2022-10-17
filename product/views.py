from contextlib import redirect_stderr
from itertools import product
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import ProductInfo
from accounts.models import UserInfo
from .forms import *
import requests

# Create your views here.

def getstart(req):
    userinfo = UserInfo.objects.get(user=req.user)
    if req.method == "POST":
        if req.user.id != None:
            product_id = req.POST.get('product_id')
            product_code = req.POST.get('product_code')

            if product_code == ProductInfo.objects.get(product_id=product_id).product_code:
                userinfo.product_id = product_id
                userinfo.device_linked = True
                userinfo.save()
                return redirect('/accounts/dashboard/' + str(userinfo.pk))
        
    return render(req, 'getstart.html', {'user':userinfo})

def userprofile(req,pk):
    userinfo = UserInfo.objects.get(pk=pk)
    if userinfo.user == req.user:
        ordered_product = OrderInfo.objects.filter(user=req.user)
        product_list = []
        for item in ordered_product:
            status = ""
            if item.order_delevered:
                status = "Delivered"
            elif item.order_delevary:
                status = "On the Way"
            elif item.order_receive:
                status = "Received"
            else:
                status = "Pending"
            product = ProductInfo.objects.get(product_id=item)
            product_dict = {'name':product.product_name, 'price':product.price, 'status':status}
            product_list.append(product_dict)
        return render(req, 'userprofile.html',{'user':userinfo, 'ordered_product':product_list})

    return render(req, 'home.html')

def productlist(req):
    products = ProductInfo.objects.filter(sold=False)
    if req.user.id != None:
        userinfo = UserInfo.objects.get(user=req.user)
    else:
        userinfo = None
        
    return render(req, 'productlist.html',{'products':products, 'user':userinfo})

def orderproduct(req, pk):
    if req.method == 'POST':
        form = OrderForm(req.POST)
        if form.is_valid():
            address = req.POST.get('address')
            contact = req.POST.get('contact')
            payment = req.POST.get('payment')
            product = ProductInfo.objects.get(pk=pk)
            product_id = product.product_id

            order =OrderInfo.objects.create(product_id=product_id)
            order.user = req.user
            order.address = address
            order.contact = contact
            order.payment = payment

            order.order_receive = False
            order.order_delevary = False
            order.order_delevered = False

            product.sold = True

            order.save()
            product.save()

            return HttpResponse('Your order is being placed')

    else:
        form = OrderForm()

        if req.user.id != None:
            userinfo = UserInfo.objects.get(user=req.user)
        else:
            userinfo = None
        product = ProductInfo.objects.get(pk=pk)

        return render(req, 'orderproduct.html',{'product':product,'user':userinfo, 'form':form})

def addproduct(req):
    if req.method == 'POST':
        form = AddProductForm(req.POST)
        if form.is_valid():
            product_name = req.POST.get('product_name')
            product_id= req.POST.get('product_id')
            price = req.POST.get('price')
            manufacturer = req.POST.get('manufacturer')
            product_code = req.POST.get('product_code')

            product = ProductInfo.objects.create(product_id=product_id)
            product.product_name = product_name
            product.price = price
            product.manufacturer = manufacturer
            product.product_code = product_code

            product.save()

            create_table_api_link = 'https://shantotech003.000webhostapp.com/create_table.php?product_id='+product_id
            api_request = requests.get(create_table_api_link)

            return HttpResponse("Successfully added the product")

    else:
        form = AddProductForm()
    return render(req, 'addproduct.html', {'form':form})
