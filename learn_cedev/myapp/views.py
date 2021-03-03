from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    id = '001'
    name = 'Atthana'
    email = 'atthana.p@codium.co'

    activities = ['Football', 'Badminton', 'Tabletennis']

    return render(request, 'index.html', {
        'id': id,
        'name': name,
        'email': email,
        'activities': activities
    })
    # มันคือให้ render ไปที่ index.html ซึ่งอยู่ที่ templates/index.html ตามที่เราตั้งไว้ที่ settings line 61 นะ


def hello(request, id):
    greeting = 'Your id: {0}'.format(id)
    return HttpResponse("<h1>Hello Q-Electronics</h1>" + greeting)


def article(request, year, slug):
    return HttpResponse('Article year = ' + str(year) + ' Slug = ' + str(slug))


def login_view(request):
    form = AuthenticationForm()
    return render(request, 'account/login.html', {
        'form': form,
    })

