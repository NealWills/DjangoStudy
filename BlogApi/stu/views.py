from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student


def index_view(request):
    method = request.method
    if method == 'GET':
        return render(request, 'register.html')
    elif method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if uname and pwd:
            student = Student(sname=uname, spwd=pwd)
            student.save()
            return HttpResponse('Regist Success')
        return HttpResponse("Regist Failure")
    else:
        return HttpResponse('Wrong, please get or post')


def show_view(request):
    # 查询表中的所有数据
    stus = Student.objects.all()
    print(stus)

    return render(request, 'show.html', {'students': stus})


def login_view(request):

    if request.method=='GET':
        return render(request, 'login.html')
    else:
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        if uname and pwd :
            count = Student.objects.filter(sname=uname, spwd=pwd).count()
            if count==1 :
                return HttpResponse('login success')
        return HttpResponse('login failed')