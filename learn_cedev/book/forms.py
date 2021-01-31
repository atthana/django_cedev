from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['id', 'slug', 'published', 'created', 'updated']  # ไม่เอาอะไรบ้าง จะตรงข้ามกับแบบเก่าที่เอาอะไรบ้าง
