from django.urls import path
from spiderman.views import *
app_name='spiderman'
urlpatterns=[
    path('aditya/',aditya,name='aditya'),
    path('neel/',neel,name='neel'),
]