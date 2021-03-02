from django.urls import path, re_path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.BookListView.as_view(), name='index'),
    # path('detail/<slug:slug>/', views.detail, name='detail'),
    path('detail/<slug:slug>/', views.BookDetailView.as_view(), name='detail'),
    # เพิ่มคำว่า detail เพื่อให้อะไรที่มีคำว่า detail ให้มาที่นี่
    re_path(r'add/$', views.book_add, name='book_add'),
]
