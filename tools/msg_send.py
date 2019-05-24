from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import random

from django.core.cache import cache


def get_code(phone):
    # 随机生成
    code = ''.join([str(random.randint(0,9)) for _ in range(4)])
    # 添加到cache缓存中
    print(code)
    cache.set(phone,code,120)  # 设置缓存cache  key 为用户手机号  value 为验证码  有效时间设置为 120 秒
    # 发送验证码
    send_sms_code(phone,code)

def confirm(phone, input_code):
    # 从缓存cache中读取phone对应的验证码
    code = cache.get(phone)
    # 和input_code进行比较，如果通过则返回True
    print(input_code,code)
    if input_code == code:
        return True
    else:
        return False


def send_sms_code(phone, code):
    # coding=utf-8

    client = AcsClient('LTAIRiQGIywYBeYN', 'ZOHiNBYPr72dCFog2fLU5Pu9RvVAIf', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "Disen工作室")
    request.add_query_param('TemplateCode', "SMS_128646125")
    request.add_query_param('TemplateParam', '{"code":"%s"}' % code)

    response = client. do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))

