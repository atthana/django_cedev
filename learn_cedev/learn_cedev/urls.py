"""learn_cedev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<int:id>', views.hello),
    re_path(r'article/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)/$', views.article)
    # year=0-9 และ 4 หลักเท่านั้น, slug=ตัว word ที่มี "-" และ + คือความยาวกี่ตัวก็ได้ "
    # test ด้วย this url "http://localhost:8000/article/2099/Q-Electronics/"
]
