from django.template import Library
import datetime

register = Library()

@register.filter()
def myCut(value):
    return ('%.2f')%value
@register.filter()
def myDut(value):
    return int(value/10000)
@register.filter()
def myEut(value):
    return value*30

@register.filter()
def myFut(value):
    return datetime.date.today()-datetime.timedelta(value)

@register.filter()
def myCut(value):
    money = str(value)[:-2][::-1]
    n=0
    m = ''
    for i in money:
        m+=i
        n+=1
        if n==3:
            m+=','
            n=0
    return m[::-1]+str(value)[-2:]
@register.filter()
def mySta(value):
    if value==1:
        return '完成'
    else:
        return '正在进行'

@register.filter()
def mytime(value:datetime):
    return str(value)[:19]


