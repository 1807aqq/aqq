import random
import uuid

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django_redis import cache

from myapp.models import User
from tools.msg_send import get_code, confirm
# from django.views.decorators.csrf import csrf_exempt

from myapp.models import User

# @csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, "enroll-1.html")
    # form = UserForm(request.POST) # 将数据传入到Form类
    # # 验证数据的完整性
    # if form.is_valid():
    #     form.save() # 无错时,则保持数据
    #     return redirect('aqq:enroll')
    # else:
    #     return render(request, 'enroll-1.html', {'errors':'<h4>验证码错误</h4>'})

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

    return render(request,'my-account.html')

def home(request):
    return render(request,"index.html")

def details(request):
    return render(request, "details.html")