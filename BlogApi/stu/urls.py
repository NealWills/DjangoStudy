#encoding=utf-8
from django.urls import path

from stu import views

urlpatterns = [
    path('', views.index_view),

    path('show/', views.show_view),
    path('login/', views.login_view)
]