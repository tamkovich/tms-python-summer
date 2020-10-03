from django.contrib import admin

from blog.models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    fields = 'title', 'description', 'author',
    search_fields = 'title',
    list_display = 'title', 'short_description', 'author', 'image', 'id'
    list_filter = 'title', 'author',


admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    fields = 'article', 'comment', 'author',
    search_fields = 'article',
    list_display = 'article', 'short_comment', 'author',
    list_filter = 'article', 'author',


admin.site.register(Comment, CommentAdmin)


