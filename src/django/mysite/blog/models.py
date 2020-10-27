from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    author_name = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)


    def __str__(self):

        return self.title




    @property
    def show_description(self):
        return self.description[:5]


class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    comment_text = models.TextField(null=True)


class Film(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    director = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=9, decimal_places=1)


    def __str__(self):

        return self.name


class Danger(models.Model):
    name = models.CharField(max_length=15)
    age = models.PositiveSmallIntegerField()
    birthday = models.DateField()



    def __str__(self):

        return self.name



class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default='anonymous')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='DataFlair Django tutorials')
    def __str__(self):
        return self.name


class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        ordering = ['created']

    class Meta:
        db_table = "blog_member"