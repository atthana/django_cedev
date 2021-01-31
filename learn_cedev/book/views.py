from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# import เข้ามาเพิ่มเพื่อจัดการกับ method 'POST' นะ
from slugify import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import BookForm
from .models import Category, Book


def index(request):
    categories = Category.objects.all()
    books = Book.objects.all().order_by('id')

    categ_id = request.GET.get('categoryid')
    if categ_id:
        books = books.filter(category_id=categ_id)

    paginator = Paginator(books, 10) # ระบุ object และจำนวนต่อเพจ
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


def detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book/detail.html', {
        'book': book
    })


def book_add(request):
    form = BookForm()

    # ส่วนที่เพิ่มขึ้นมา เพื่อมาเช็ค form ที่ post เข้ามาจาก FE นะ (code ในการ add, save ข้อมูลลง db)
    # พอเรากดปุ่ม save book มันจะวิ่งกลับมาที่ function เดิมของมันคืออันนี้ เราจึงต้องมาเช็ค if ที่นี่
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # ถ้า post เข้ามาก้อมาอ่านข้อมูลจาก request ทั้งข้อความและไฟล์อัพโหลดด้วย พออ่านเสร็จก้อ generate กลับมาให้อยู่ในรูปของ object form เหมือนเดิมนะ
        if form.is_valid():  # มา validate ต่อว่าฟอห์มถูกต้องรึป่าว default จะ validate จากค่า null+blank, โดย default จะ validate จากค่า blank เป็นหลัก
            book = form.save(commit=False)  # ถ้า validate ผ่านนะจึงมาทำต่อที่นี่ สร้าง object book จาก form โดย save แบบหลอกๆให้กลายเป็น object book นะ (พูดง่ายๆคือ เปลี่ยน form ให้เป็น object book นะ)
            book.slug = slugify(book.name)  # gen slug ขึั้นมาใส่ใน book.slug (ใช้ lib ช่วยนะ)
            book.published = True  # หนังสือใหม่ที่เราจะเซฟ ให้เป็น auto publish นะ
            book.save()  # พอพร้อมหมดแล้วก้อให้ save ข้อมูล
            form.save_m2m()  # ถ้า book เรามีการใช้ author ซึ่งเป็นแบบ many to many นะ จะต้องใช้ .save_m2m() ด้วยนะ เป็นคำสั่งในการ save field ในฝั่ง many
            messages.success(request, 'Save success')  # ถ้า save สำเร็จก้อให้มันส่ง message กลับไปที่หน้าจอให้ user รู้
            return HttpResponseRedirect(reverse('book:index', kwargs={})) # พอ save ผ่าน ก็ redirect กลับไปที่หน้า index และไม่ได้ส่ง param อะไรกลับไปนะ เลยเป็น dict ว่างๆ
        messages.error(request, 'Save failed !')  # กรณี save fail ก็ให้ส่ง message กลับไปโชว์นะ

    return render(request, 'book/add.html', {  # โดยถ้า save fail, message ก้อจะกลับมาโชว์ที่เดิมนะ โดย code ชุดนี้จะไม่ทำนะ กรณี success เพราะได้ return redirect ไปก่อนแล้ว
        'form': form
    })