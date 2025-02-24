from django.contrib import admin
from django.urls import path
from .views import login_user, register_user, logout_user, menu_user



urlpatterns = [
    path('', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('logout/', logout_user, name='logout_user'),
    path('menu/', menu_user, name='menu_user')
]
