from django.urls import path

from myapp.views import *

app_name = 'aqq'
urlpatterns = [
    path('account/', my_account,name='account'),
    path('enroll/', register, name='enroll'),
]