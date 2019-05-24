from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from myapp.models import User

LOGIN_REQUIRED = ['/aqq/account/']

class LoginMiddleware(MiddlewareMixin):  # 自定义登录中间件
    def process_request(self,request):
        if request.path in LOGIN_REQUIRED:

            user_id = request.session.get('user_id')
            if user_id:
                user = User.objects.get('pk=id')  # 查出当前用户
                request.user = user  # 给request请求对象动态添加user属性，属性为当前登录的用户
            else:
                messages.add_message(request,level=messages.INFO,message='您还未登录!!')

                return redirect(reverse('aqq:login'))
