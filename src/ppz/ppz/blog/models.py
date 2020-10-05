from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    author_name = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)

    @property
    def short_description(self):
        return self.description[:1]


    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    author_name = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)



    @property
    def short_description(self):
        return self.description[:1]


    def __str__(self):
        return self.title
