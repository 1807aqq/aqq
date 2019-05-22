from django.shortcuts import render
from tonghuashun.news import *
from myapp.models import User,industry
from tools.msg_send import get_code, confirm


def register(request):
    if request.method == "GET":
        return render(request, "enroll-1.html")
    elif request.method == "POST":
        phone = request.POST.get("phone") # 获取手机号

        # phone-message # 短信验证码
        phone_message = request.POST.get('phone-message')
        get_code(phone)
        if not confirm(phone, phone_message):
            return render(request, "enroll-1.html")


        pw = request.POST.get('pw') # 获取密码
        identity = request.POST.get('identity') # 获取用户身份证号
        bank_num = request.POST.get('infos') # 获取用户银行卡号
        banks = request.POST.get('category') # 获取用户银行名称
        city = request.POST.get('city') # 获取用户所在地
        open_bank = request.POST.get('open_bank')
        print(phone,pw,identity,bank_num,banks,city,open_bank)
        # new_user = User()
        # new_user.phone = phone
        # new_user.passwd = pw
        # new_user.identity =identity
        # new_user.bank_num = bank_num
        # new_user.banks = banks
        # new_user.city = city
        # new_user.open_bank = open_bank



def my_account(request):

    return render(request,'my-account.html')

# 进入首页
def go_index(request):
    if request.method =='GET':
        url = 'http://www.10jqka.com.cn/'
        datas = Downlode(url)
        all = industry.objects.all()
        all.delete()
        print('-********-----*********---',datas)
        for msg in datas:
            industry.info = msg.get('info')
            industry.name = msg.get('title')
            industry.time = msg.get('news_time')

        return render(request,'index.html',datas)

#进入新闻详情页

def go_details(request):
    id = request.GET.get('id')
    msg = industry.objects.filter(id=id)
    print(msg)
    return render(request,'press-details.html')


