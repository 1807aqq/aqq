from django.shortcuts import render, redirect
# from myapp.forms import UserForm
# from myapp.models import User
# from tools.msg_send import get_code, confirm


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

def home(request):
    return render(request,"index.html")

def details(request):
    return render(request, "details.html")