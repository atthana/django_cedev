from django.shortcuts import render
from .models import Category, Book


def index(request):
    categories = Category.objects.all()
    books = Book.objects.all().order_by('id')
    return render(request, 'book/index.html', {
        'categories': categories,
        'books': books,
    })