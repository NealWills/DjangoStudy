from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student


def index_view(request):

    method = request.method
    if method=='GET':
        return render(request, 'register.html')
    elif method=='POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if uname and pwd:
            student = Student(sname=uname, spwd=pwd)
            student.save()
            return HttpResponse('Regist Success')
        return HttpResponse("Regist Failure")
    else:
        return HttpResponse('Wrong, please get or post')