from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Comment
from .models import Film
from .models import Danger


class Article_Admin(admin.ModelAdmin):
    fields = ('title', 'description', 'image')
    search_fields = 'title',


class made_of_COMMENT(admin.ModelAdmin):
    pass

class Made_of_film(admin.ModelAdmin):
    pass

class Danger_admin(admin.ModelAdmin):
    fields = ('name', 'age', 'photo')

admin.site.register(Article, Article_Admin)
admin.site.register(Comment, made_of_COMMENT)
admin.site.register(Film, Made_of_film)
admin.site.register(Danger, Danger_admin)

