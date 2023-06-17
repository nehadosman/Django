from django.contrib import admin

from .models import Book, Category, ISBN



# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name')

class StackedISBNInline(admin.StackedInline):
    model = ISBN

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'rate', 'views')
    list_filter = ('categories', 'user')
    inlines = [StackedISBNInline]

    def has_add_permission(self, request):
        print(2222222222222)
        if request.user.is_superuser:
            return True
        return False

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ISBN)
class ISBNAdmin(admin.ModelAdmin):
    list_display = ('author_title', 'book_title', 'isbn_number', 'book')
