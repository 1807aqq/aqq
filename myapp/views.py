from django.shortcuts import render
from tonghuashun.news import *
from myapp.models import User, Industry
from tools.msg_send import get_code, confirm
import time

def register(request):
    if request.method == "GET":
        return render(request, "enroll-1.html")
    # form = UserForm(request.POST) # 将数据传入到Form类
    # # 验证数据的完整性
    # if form.is_valid():
    #     form.save() # 无错时,则保持数据
    #     return redirect('/')
    # return render(request, 'enroll-1.html', locals())


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

def details(request):
    return render(request, "details.html")
