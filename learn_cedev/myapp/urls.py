from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<int:id>', views.hello, name='hello2'),
    re_path(r'article/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)/$', views.article, name='article')

    # year=0-9 และ 4 หลักเท่านั้น, slug=ตัว word ที่มี "-" และ + คือความยาวกี่ตัวก็ได้ "
    # test ด้วย this url "http://localhost:8000/article/2099/Q-Electronics/"
]