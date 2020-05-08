import math

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from movie.models import Movie


def pageset(page, row=20):
    num = int(page)
    if num < 1:
        num = 1
    totolRecords = Movie.objects.count()
    totolPages = int(math.ceil(totolRecords * 1.0 / row))
    if num > totolPages:
        num = totolPages
    movies = Movie.objects.all()[((num - 1) * row):(num * row)]
    return movies, num


def index_view(request):
    if request.method == 'GET':

        page = request.GET.get('page')
        row = request.GET.get('row')
        # print(page, row)

        movies, num = pageset(int(page), int(row))
        countCurrent = int(num) % int(row)

        return HttpResponse(movies)
    else:
        page = request.POST.get('page')
        row = request.POST.get('row')
        print(page, row)
        # movies, num = pageset(page, row)
        # countCurrent = num % row

        return HttpResponse('movies')
