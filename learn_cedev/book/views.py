from django.shortcuts import render
from .models import Category, Book


def index(request):
    categories = Category.objects.all()
    books = Book.objects.all().order_by('id')

    categ_id = request.GET.get('categoryid')
    print(categ_id)
    print(type(categ_id))
    if categ_id:
        books = books.filter(category_id=categ_id)

    return render(request, 'book/index.html', {
        'categories': categories,
        'books': books,
        'categ_id': categ_id,
    })