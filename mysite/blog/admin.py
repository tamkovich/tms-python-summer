from django.contrib import admin

from blog.models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    fields = 'title', 'description', 'author',
    search_fields = 'title',
    list_display = 'title', 'short_description', 'author', 'image', 'id',
    list_filter = 'title', 'author',


admin.site.register(Article, ArticleAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = 'name', 'email', 'article', 'created', 'active'
    list_filter = 'active', 'created', 'updated'
    search_fields = 'name', 'email', 'body'


# class CommentAdmin(admin.ModelAdmin):
#     fields = 'article', 'text', 'author',
#     search_fields = 'article',
#     list_display = 'article', 'short_text', 'author',
#     list_filter = 'article', 'author',
#
#
# admin.site.register(Comment, CommentAdmin)


