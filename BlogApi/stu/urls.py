#encoding=utf-8
from django.urls import path

from stu import views

urlpatterns = [
    path('', views.index_view)
]