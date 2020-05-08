#coding=utf-8

from django.urls import path

from movie import views

urlpatterns = [
    path('', views.index_view)
]