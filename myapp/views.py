import random

from tonghuashun.news import *

from myapp.models import *
from tools.msg_send import get_code, confirm

import time

from django.shortcuts import render, redirect


from myapp.models import User


def register(request):
    if request.method == "GET":
        return render(request, "enroll-1.html")
    phone = request.POST.get('phone')
    phone_message = request.POST.get('phone-message')
    nickname = request.POST.get('nickname')
    passwd = request.POST.get('pw')
    name = request.POST.get('realname')
    identity = request.POST.get('identity')
    bank_num = request.POST.get('bank_num')
    banks = request.POST.get('category')
    city = request.POST.get('city')
    open_bank = request.POST.get('open_bank')
    print(phone,phone_message,passwd,name,identity,bank_num,banks,city,open_bank)
    new_user = User()
    new_user.nickname = nickname
    new_user.phone = phone
    new_user.passwd =passwd
    new_user.name = name
    new_user.identity = identity
    new_user.bank_num = bank_num
    new_user.banks = banks
    new_user.city = city
    new_user.open_bank = open_bank
    new_user.save()
    return redirect("aqq:account")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":
        phone = request.POST.get('name')
        passwd = request.POST.get('password')
        print(phone,passwd,"@@@@@@@@@@@2")
        if User.objects.filter(phone=phone, passwd=passwd).exists():
            return render(request, 'my-account.html')


def my_account(request):
    return render(request, 'my-account.html')


# 进入首页
def go_index(request):
    if request.method == 'GET':
        now_time = time.localtime().tm_min
        if now_time%10 == 0:
            Downlode()
        datas = Industry.objects.all()
        msgs = {}

        for data in datas:
            db = {}
            db['ip'] = data.ip
            db['title'] = data.name
            db['news_time'] = data.time
            msgs[data.ip] = db
        return render(request, 'index.html', {'datas':msgs})


# 进入新闻详情页
def go_details(request,id):
    msg = Industry.objects.filter(ip=id)[0]
    title = msg.name
    time = msg.time
    info = base64.b16decode((msg.info).encode()).decode()
    return render(request, 'press-details.html',locals())

# 新闻中心
def press_center(request):
    datas = Industry.objects.all()
    msgs = {}
    for data in datas:
        db = {}
        msg = base64.b16decode(data.info.encode()).decode()
        db['ip'] = data.ip
        db['info'] = ','.join(re.findall(r'[\u4e00-\u9fa5]{10}',msg))[:50]
        db['title'] = data.name
        msgs[data.ip] = db
    return render(request, 'press-center.html', {'datas': msgs})

# 投资理财页面
def invest(request,tid,sid,did):
    if request.method == 'GET':
        pass



        data = {

            'tid':0,
            'sid':0,
            'did':0
        }


    products = Product.objects.order_by('id')[:7]
    organization = Institutions.objects.all()
    for product in products:
        in_name = random.choice(organization).name
    return render(request,'invest.html',locals())



# 首页产品
def index_view(request):
    products = Product.objects.order_by('-id')[:3]
    products1 = Product.objects.order_by('-id')[4:7]
    for product1 in products1:
        return render(request,'index.html', locals())


def details(request):
    return render(request, "details.html")
