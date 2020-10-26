from django.contrib import admin

from blog.models import Article, Comment, Category


class ArticleAdmin(admin.ModelAdmin):
    fields = 'title', 'description', 'author', 'category', 'image',
    search_fields = 'title', 'category', 'published',
    list_display = 'title', 'short_description', 'author', 'category', 'image', 'published', 'id',
    list_filter = 'title', 'author', 'category',


admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    fields = 'text', 'author', 'article', 'created', 'active',
    list_display = 'short_text', 'author', 'article', 'created', 'active',  'id',
    list_filter = 'active', 'created', 'author', 'article',
    search_fields = 'author', 'article', 'created',


admin.site.register(Comment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = 'title', 'description',
    list_display = 'title', 'description', 'id',
    search_fields = 'title',


admin.site.register(Category, CategoryAdmin)




