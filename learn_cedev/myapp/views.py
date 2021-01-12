from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
    # มันคือให้ render ไปที่ index.html ซึ่งอยู่ที่ templates/index.html ตามที่เราตั้งไว้ที่ settings line 61 นะ


def hello(request, id):
    greeting = 'Your id: {0}'.format(id)
    return HttpResponse("<h1>Hello Q-Electronics</h1>" + greeting)


def article(request, year, slug):
    return HttpResponse('Article year = ' + str(year) + ' Slug = ' + str(slug))

