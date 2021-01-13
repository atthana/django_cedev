from django.contrib import admin
from .models import Category, Author, Book, BookComment


class BookCommentStackedInline(admin.StackedInline):
    model = BookComment  # บอกมันว่าจะเอา model ไหนมาทำ


class BookTabularInline(admin.TabularInline):
    model = BookComment
    extra = 2
    # คือมันจะจองพื้นที่ด้านล่างของ comment ให้เราเป็นจำนวน line นะ ใช้แทนกันได้อยู่ที่ความสบายตา ระหว่าง StackedInline กับ TabularInline


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
    inlines = [BookTabularInline]


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
