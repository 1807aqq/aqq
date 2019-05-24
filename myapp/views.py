

from django.db.models import Q

from tonghuashun.news import *

from myapp.models import User, Industry ,Product ,Institutions

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
        new_pro = Product.objects.filter(type=1)
        for data in datas:
            db = {}
            db['ip'] = data.ip
            db['title'] = data.name
            db['news_time'] = data.time
            msgs[data.ip] = db
        return render(request, 'index.html', {'datas':msgs,'new_pros':new_pro[:3],'pros':new_pro[5:8]})


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
def invest(request,tid,sid,did,page):
    if request.method == 'GET':
        type_list = ['type=1','type=2','type=3','type=4','type=5']
        rate_list = ['y_rate__lt=11', 'y_rate__gt=11,y_rate__lt=13', 'y_rate__gt=13']
        time_list = ['time_limit=24', 'time_limit=36', 'time_limit=48']
        select = {
            'tid': [tid,type_list],
            'sid': [sid,rate_list],
            'did': [did,time_list]
        }
        filters = []
        for k in select:
            if select[k][0] == '0':
                continue
            else:
                filters.append(select[k][1][int(select[k][0])-1])
        data = {}
        m = int(page) * 8
        if len(filters) > 0:
            for i in filters:
                if ',' in i:
                    x,y = i.split(',')
                    a,b = x.split('=')
                    data[a]=b
                    a,b = y.split('=')
                    data[a]=b
                else:
                    a,b = i.split("=")
                    data[a]=b
            print(data)
            produces = Product.objects.filter(**data)[m-8:m]

        else:
            produces = Product.objects.all()[m-8:m]

        data = {
            'products': produces,
            'tid': tid,
            'sid': sid,
            'did': did,
            'page':page
        }
        return render(request,'invest.html',data)




# 首页产品
def index_view(request):
    products = Product.objects.order_by('-id')[:3]
    products1 = Product.objects.order_by('-id')[4:7]
    for product1 in products1:
        return render(request,'index.html', locals())

# 产品详情页
def details(request,pid):
    pro = Product.objects.get(id=int(pid))
    pay = ['先息后本','先本后息','等额本金','等额本息']
    payment = pay[pro.payment-1]
    data = pro.info.split('&')
    print(payment)
    data1 = data[0]
    data2 = data[1]
    data3 = data[2]
    return render(request, "details.html",
                  {'pro':pro,
                   'payment':payment,
                   'data1':data1,
                   'data2':data2,
                   'data3':data3})
# 安全保障
def secure(request):
    return render(request,'secure.html')

# 关于我们
def anenst(request):
    return render(request,'anenst.html')

# 新手指南
def  guide(request):
    return  render(request,'Beginners-Guide.html')