from django.shortcuts import render
from django.http import HttpResponse


def hello(request, id):
    greeting = 'Your id: {0}'.format(id)
    return HttpResponse("<h1>Hello Q-Electronics</h1>" + greeting)


def article(request):
    return HttpResponse('Article')

