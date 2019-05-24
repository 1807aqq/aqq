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

