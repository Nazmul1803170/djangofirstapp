from http.client import HTTPResponse
from django.shortcuts import render,redirect
from accounts.models import UserInfo
from django.contrib.auth.models import AnonymousUser
from product.models import OrderInfo

def home(req):
    user = req.user
    if user.id == None:
        return render(req, 'home.html')
    else:
        userinfo = UserInfo.objects.get(user=req.user)
        if userinfo.device_linked:
            return redirect('/accounts/dashboard/' + str(userinfo.pk))
        elif userinfo.is_admin:
            return redirect('/adminpage/' + str(userinfo.pk))
        else:
            return redirect('/product/userprofile/' + str(userinfo.pk))

def adminview(req,pk):
    userinfo = UserInfo.objects.get(pk=pk)
    if userinfo.user == req.user:
        pen_product = OrderInfo.objects.filter(order_delevered = False)
        products = []
        pdt = {}
        for pdt_item in pen_product:
            pdt = vars(pdt_item)
            username = UserInfo.objects.get(user=pdt_item.user).name
            pdt['username'] = username
            products.append(pdt)
        
        return render(req, 'admin.html',{'products':products, 'user':userinfo})

def receivedview(req,pi):
    userpk = UserInfo.objects.get(user=req.user).pk
    order = OrderInfo.objects.get(product_id=pi)
    order.order_receive = True
    order.save()
    return redirect('/adminpage/'+str(userpk))

def delivaryview(req,pi):
    userpk = UserInfo.objects.get(user=req.user).pk
    order = OrderInfo.objects.get(product_id=pi)
    order.order_delevary = True
    order.save()
    return redirect('/adminpage/'+str(userpk))

def handoverview(req,pi):
    userpk = UserInfo.objects.get(user=req.user).pk
    order = OrderInfo.objects.get(product_id=pi)
    order.order_delevered = True
    order.save()
    return redirect('/adminpage/'+str(userpk))


def chartview(req):
    return render(req, 'chartview.html')
