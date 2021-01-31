from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['id', 'slug', 'published', 'created', 'updated']  # ไม่เอาอะไรบ้าง จะตรงข้ามกับแบบเก่าที่เอาอะไรบ้าง

    def __init__(self, *args, **kwargs):  # อันนี้เป็น pattern ของการทำ function hook นะ (custom validator)
        super(BookForm, self).__init__(*args, **kwargs) # ไปอ่านข้อมูลจาก BookForm มา และส่ง parameter ตัวเดิมกลับไปนะ
        self.fields['code'].error_messages = {
            'required': 'Please enter book code',
        }
        self.fields['name'].error_messages = {
            'required': 'Please enter book name',
        }
        self.fields['price'].error_messages = {
            'required': 'Please enter book price',
            'invalid': 'Please enter a valid book price'
        }

    def clean(self):  # เป็นการ hook function clean() มาใช้ 
        cd = super(BookForm, self).clean()
        if not cd.get('category'):  # ถ้าไม่่มี key 'category' นะก้อค่อยทำ
            self.add_error('category', 'Please select category name')
        if not cd.get('author'):
            self.add_error('author', 'Please choose an author name')