from django.urls import path

from myapp.views import *

app_name = 'aqq'
urlpatterns = [
    path('account/', my_account,name='account'),
    path('enroll/', register, name='enroll'),
    path('home/',go_index,name='home'),
    path('details/<id>/',go_details,name = 'details'),
    path('center/',press_center,name='center'),
    path('invest/<tid>/<sid>/<did>/<page>/',invest,name= 'invest'),
    path('product/<pid>/',details,name='product'),
    path('borrow/',borrow_money,name='borrow'),
    path('secure/',secure,name='secure'),
    path('anenst/',anenst,name='anenst'),
    path('guide/',guide,name='guide'),
    path('help/',help,name='help'),
    path('recharge/',recharge,name='recharge'),
    path('withdraw/',withdraw,name='withdraw'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('getcode/<phone>/',codes,name='codes'),
    path('pledge/',pledge,name='pledge'),
    path('mortgage/',mortgage,name='mortgage'),
    path('venture/',venture,name='venture'),
    path('policy/',policy,name='policy'),
    path('logout/',logout,name='logout'),
    path('buy/<pid>/',buy,name='buy')

]

