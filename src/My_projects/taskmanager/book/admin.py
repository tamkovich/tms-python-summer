from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    fields = 'title', 'description', 'author',
    search_fields = 'title',
    list_display = 'title', 'short_description', 'author', 'id',
    list_filter = 'title', 'author',


admin.site.register(Book, BookAdmin)
