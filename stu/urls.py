#coding=utf-8
from django.urls import path

from stu import views

urlpatterns = {
    path('login', views.login_view)
}