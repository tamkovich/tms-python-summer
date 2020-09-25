from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField('book_title', max_length=250)
    description = models.TextField('book_description')
    author = models.CharField('book_author', max_length=50)
    id = models.AutoField(primary_key=True)

    @property
    def short_description(self):
        return self.description[:50]

    def __str__(self):
        return self.title