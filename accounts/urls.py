from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path("", views.index, name='accounts'),
    path("login/", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("register/", views.register, name='register')

]