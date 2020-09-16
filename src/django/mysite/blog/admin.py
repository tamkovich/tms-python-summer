from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Comment


class Article_Admin(admin.ModelAdmin):
    fields = ('title', 'description')
    search_fields = 'title',


class made_of_COMMENT(admin.ModelAdmin):
    pass


admin.site.register(Article, Article_Admin)
admin.site.register(Comment, made_of_COMMENT)
