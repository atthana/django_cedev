from django.db import models

BOOK_LEVEL_CHOICE = (  # โชว์ชุดหลัง แต่เซฟด้วยชุดหน้า เช่น โชว์ Basic แต่เซฟด้วย B นะ
    ('B', 'Basic'),
    ('M', 'Medium'),
    ('A', 'Advance'),
)

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Author"

    def __str__(self):
        return self.name


class Book(models.Model):
    code = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author, blank=True)
    level = models.CharField(max_length=5, null=True, blank=True, choices=BOOK_LEVEL_CHOICE)   # เอา choices จากข้างบนมาใช้
    image = models.FileField(upload_to='upload', null=True, blank=True)  # รูปจะถุกเก็บเข้า folder "upload" อัตโนมัติ
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-code']  # ถ้ามีติดลบนำหน้า คือเรียงจากมากไปน้อย
        verbose_name_plural = "Book"

    def __str__(self):
        return self.name


class BookComment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']  # เรียงตาม id จากน้อยไปมาก (id ไม่มีใน Model แต่ Django สร้างให้เราแล้วนะ)
        verbose_name_plural = "Book Comment"

    def __str__(self):
        return self.comment

