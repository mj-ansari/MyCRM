from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='home'),
    path('logout_user/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('customer/<int:pk>', customer, name='customer'),
    path('add_customer/', add_customer, name='add_customer'),
    path('update_customer/<int:pk>', update_customer, name='update_customer'),
    path('delete_customer/<int:pk>', delete_customer, name='delete_customer'),
]
