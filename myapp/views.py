
from django.shortcuts import render
from tonghuashun.news import *
from myapp.models import User,Industry
from tools.msg_send import get_code, confirm


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

    return render(request,'my-account.html')


# 进入首页
def go_index(request):
    if request.method =='GET':
        url = 'http://www.10jqka.com.cn/'
        datas = Downlode(url)
        all = Industry.objects.all()
        all.delete()
        print('-********-----*********---',datas)
        for msg in datas:
            Industry.info = msg.get('info')
            Industry.name = msg.get('title')
            Industry.time = msg.get('news_time')

        return render(request,'index.html',datas)

#进入新闻详情页

def go_details(request):
    id = request.GET.get('id')
    msg = Industry.objects.filter(id=id)
    print(msg)
    return render(request,'press-details.html')



def details(request):
    return render(request, "details.html")

