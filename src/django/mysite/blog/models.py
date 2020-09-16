from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.



class Article(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    author_name = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):

        return self.title


    @property
    def show_description(self):
        return self.description[:5]


class Comment(models.Model):

    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

