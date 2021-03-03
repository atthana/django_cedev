from django.contrib.auth import login
from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # จะได้ user มา
            login(request, user)  # เรียกใช้ฟังก์ชัน login โดยส่ง request กับ user ไป
            return redirect('book:index')  # เพื่อให้ง่าย django ก้อมี shortcut redirect() ให้เราวิ่งไปที่ index.html ต่อเลย
    else:
        form = AuthenticationForm()  # คือถ้า else ก้อให้สร้าง form ว่างๆ
    return render(request, 'account/login.html', {
        'form': form,
    })

