
from django.db.models import Q, Sum, Count, F
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse

from tonghuashun.news import *

from myapp.models import User, Industry, Product, Institutions, Investment

from tools.msg_send import get_code, confirm
from tools.Is_login import is_login
import time

from django.shortcuts import render, redirect

from myapp.models import User

# 注册页面
def register(request):
    if request.method == "GET":
        # msg = messages.get_messages(request)
        # context = {'msg':None}
        return render(request, "enroll-1.html")
    elif request.method == 'POST':
        phone = request.POST.get('phone')
        print(phone)
        print(User.objects.filter(phone=phone))
        if User.objects.filter(phone=phone).exists():
            print('=====ddd====')
            messages.add_message(request, messages.INFO, '该手机号已注册！！')
            return redirect('aqq:register')
        phone_message = request.POST.get('phone-message')
        code = confirm(phone,phone_message)
        print(code)
        if not code:
            messages.add_message(request, messages.INFO, '验证码错误！！')
            return redirect('aqq:register')
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

# 登陆页面
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        phone = request.POST.get('name')
        passwd = request.POST.get('password')
        print(phone,passwd,"@@@@@@@@@@@2")
        if User.objects.filter(phone=phone, passwd=passwd).exists():
            user = User.objects.filter(phone=phone, passwd=passwd)[0]
            if phone == user.phone and passwd == user.passwd:
                request.session['uid'] = user.uid
                return redirect(reverse('aqq:account'))
            else:
                context = {'msg':'用户名或密码错误！！！'}
                return render(request,'login.html',context)

        else:
            messages.add_message(request,messages.INFO,'用户名不存在！！')
            return redirect('aqq:register')


def my_account(request):
    user = is_login(request)
    return render(request, 'my-account.html',{'user':user})


# 进入首页
def go_index(request):
    user = is_login(request)
    print('@@@@@@@@@@@',user)
    if request.method == 'GET':
        now_time = time.localtime().tm_min
        if now_time%10 == 0:
            Downlode()
        datas = Industry.objects.all()
        sum_amount = Product.objects.all().aggregate(Sum('amount'))
        count = Product.objects.all().aggregate(Count('name'))
        msgs = {}
        new_pro = Product.objects.filter(type=1)
        for data in datas:
            db = {}
            db['ip'] = data.ip
            db['title'] = data.name
            db['news_time'] = data.time
            msgs[data.ip] = db
        return render(request, 'index.html',
                      {'datas':msgs,
                       'new_pros':new_pro[:3],
                       'pros':new_pro[5:8],
                      'sum_amount':sum_amount,
                       'count':count,
                       'user':user})





# 进入新闻详情页
def go_details(request,id):
    user = is_login(request)
    msg = Industry.objects.filter(ip=id)[0]
    title = msg.name
    time = msg.time
    info = base64.b16decode((msg.info).encode()).decode()
    return render(request, 'press-details.html',locals())

# 新闻中心
def press_center(request):
    user = is_login(request)
    datas = Industry.objects.all()
    msgs = {}
    for data in datas:
        db = {}
        msg = base64.b16decode(data.info.encode()).decode()
        db['ip'] = data.ip
        db['info'] = ','.join(re.findall(r'[\u4e00-\u9fa5]{10}',msg))[:50]
        db['title'] = data.name
        msgs[data.ip] = db
    return render(request, 'press-center.html', {'datas': msgs,'user':user})

# 投资理财页面
def invest(request,tid,sid,did,page):
    user = is_login(request)
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
        newpage = int(page)
        m = newpage * 8
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
        newpage +=1
        balances = []
        for produce in produces:
            inv = Investment.objects.filter(pid=produce.id)
            if inv.exists():
                print(inv.aggregate(Sum('amount')))
                balance = produce.amount - (inv.aggregate(Sum('amount'))['amount__sum']) / 10000

            else:
                balance = produce.amount

            produce.balance = balance
        data = {
            'products': produces,
            'tid': tid,
            'sid': sid,
            'did': did,
            'page':newpage,
            'user':user,

        }
        return render(request,'invest.html',data)



# 产品详情页
def details(request,pid):
    user = is_login(request)
    pro = Product.objects.get(id=int(pid))
    pay = ['先息后本','先本后息','等额本金','等额本息']
    payment = pay[pro.payment-1]
    data = pro.info.split('&')
    inv = Investment.objects.filter(uid=user.uid,pid=pro.id)
    if inv.exists() :
        print(inv)
        balance = pro.amount - (inv.first().amount)/10000
    else:
        balance = pro.amount
    data1 = data[0]
    data2 = data[1]
    data3 = data[2]
    return render(request, "details.html",
                  {'pro':pro,
                   'payment':payment,
                   'data1':data1,
                   'data2':data2,
                   'data3':data3,
                   'user':user,
                   'balance':balance})
#投资输入金额

def buy(request,pid):
    user = is_login(request)
    if request.method == 'GET':
        if user.em_contact == None:
            money = 0.0
        else:
            money = user.em_contact
        return render(request,'buy.html',{'user':user,'money':money,'pid':pid})
    elif request.method == 'POST':
        pro = Product.objects.get(id=pid)
        buy_money = request.POST.get('money')
        if user.em_contact > int(buy_money) \
                and int(buy_money)< (pro.amount)*10000:
            try:
                user.em_contact=F('em_contact')-int(buy_money)

                inv = Investment.objects.filter(pid=pid, uid=user.uid)
                if inv.exists():
                    #inv.update(amount=F('amount')+int(buy_money))  第一种可以
                    a = inv.first()
                    a.amount = F('amount')+int(buy_money)
                    a.save()

                else:
                    inv = Investment.objects.create(uid=user.uid,pid=pid,amount=int(buy_money))
                    inv.save()
                user.save()
                code = 200
                msg = '投资成功'
            except Exception as e:
                print(e)
                code = 400
                msg = '投资失败'
        else:

            code=300
            msg = '余额不足'

        return JsonResponse({
                    'code':code,
                    'msg':msg
                    })

# 安全保障
def secure(request):
    user = is_login(request)
    return render(request,'secure.html',{'user':user})

# 关于我们
def anenst(request):
    user = is_login(request)
    return render(request,'anenst.html',{'user':user})



# 借贷专区

def borrow_money(request):
    user = is_login(request)
    return render(request,'borrow-money.html',{'user':user})

# 新手指南
def  guide(request):
    user = is_login(request)
    return  render(request,'Beginners-Guide.html',{'user':user})

#帮助中心
def help(request):
    user = is_login(request)
    return  render(request,'help-center.html',{'user':user})

# 充值
def recharge(request):
    user = is_login(request)
    return render(request,'my-recharge.html',{'user':user})

#提现
def withdraw(request):
    user = is_login(request)
    return render(request,'my-withdraw.html',{'user':user})


# 发送验证码函数
def codes(request,phone):
    user = is_login(request)
    get_code(phone)
    return JsonResponse({
        'code': 200,
    })

# 申请质押贷款
def pledge(request):
    user = is_login(request)
    if request.method == 'GET':
        return render(request,'Pledge-loan.html',{'user':user})
    elif request.method == 'POST':
        if request.user:
            pass
        else:
            data={
                'msg':'您还未登录！！',
                'user': user
            }
    return render(request,'Pledge-loan.html',data)

# 申请抵押贷
def mortgage(request):
    user = is_login(request)
    if request.method == 'GET':
        return render(request,'mortgage-loan.html',{'user':user})
    elif request.method == 'POST':
        if request.user:
            pass
        else:
            data={
                'msg':'您还未登录！！',
                'user': user
            }
    return render(request,'mortgage-loan.html',data)


# 申请创业贷
def venture(request):
    user = is_login(request)
    if request.method == 'GET':
        return render(request,'Venture-loan.html',{'user':user})
    elif request.method == 'POST':
        if request.user:
            pass
        else:
            data={
                'msg':'您还未登录！！',
                'user': user
            }
    return render(request,'Venture-loan.html',data)

# 申请保单贷
def policy(request):
    user = is_login(request)
    if request.method == 'GET':
        return render(request,'Policy-loan.html',{'user':user})
    elif request.method == 'POST':
        if request.user:
            pass
        else:
            data={
                'msg':'您还未登录！！',
                'user': user
            }
    return render(request,'Policy-loan.html',data)

def logout(request):
    request.session.flush()
    return redirect(reverse('aqq:home'))