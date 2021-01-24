from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Book


def index(request):
    categories = Category.objects.all()
    books = Book.objects.all().order_by('id')

    categ_id = request.GET.get('categoryid')
    if categ_id:
        books = books.filter(category_id=categ_id)

    paginator = Paginator(books, 2) # ระบุ object และจำนวนต่อเพจ
    print("paginator = ", paginator)
    page = request.GET.get('page')
    print("page = ", page)
    # breakpoint()
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)  #  ถ้าหน้าเพจมีปัญหาก้อให้มันอยู่ที่เพจ 1 เสมอ
    except EmptyPage:  # หน้าสุดท้ายหรือหน้าน้อยเกินไปก็ให้ดึงข้อมูลทั้งหมดมาใส่ในตัวแปร books 
        books = paginator.page(paginator.num_pages)

    return render(request, 'book/index.html', {
        'categories': categories,
        'books': books,
        'categ_id': categ_id,
    })