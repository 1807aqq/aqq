from django.urls import path

from myapp.views import my_account, register

app_name = 'aqq'
urlpatterns = [
    path('account/', my_account,name='account'),
    path('enroll/', register, name='enroll'),
]