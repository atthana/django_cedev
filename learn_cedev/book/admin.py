from django.contrib import admin
from .models import Category, Author, Book, BookComment


class BookCommentStackedInline(admin.StackedInline):
    model = BookComment  # บอกมันว่าจะเอา model ไหนมาทำ


class BookAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'price', 'published']
    list_filter = ['published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug': ['name']}
    # สร้าง slug จาก field 'name' เวลาเราเพ่ิมข้อมูลใน Name ข้อมูลจะเพิ่มใน Slug: ให้เลยอัตโนมัติโดยเอา space มาแทนด้วย "-" นะ
    fieldsets = (
        (None, {'fields':['code', 'slug', 'name', 'description', 'price', 'published']}),
        ('Category', {'fields': ['category', 'author'], 'classes': ['collapse']}),
    )
    # fieldsets เป็นการจัดกลุ่มให้เป็น set นะในหน้า admin เพื่อให้ไม่รกตาเกินไป
    inlines = [ BookCommentStackedInline ]


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
