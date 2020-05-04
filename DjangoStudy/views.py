#coding=utf-8

from django.http import HttpResponse

#显示 Hello world
def index_view(request):

    return HttpResponse('Hello World')
