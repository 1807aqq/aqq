from django.urls import path

from myapp.views import *

app_name = 'aqq'
urlpatterns = [
    path('account/', my_account,name='account'),
    path('enroll/', register, name='enroll'),
    path('home/',go_index,name='home'),
    path('details/<id>/',go_details,name = 'details'),
    path('center/',press_center,name='center'),
    path('invest/<tid>/<sid>/<did>/',invest,name= 'invest')
]