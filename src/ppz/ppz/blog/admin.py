from django.contrib import admin
from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):

    search_fields = ('title', 'short_description', 'author',)
    list_display = 'title', 'short_description', 'author_name', 'author'
    list_filter = 'title',




admin.site.register(Article, ArticleAdmin)