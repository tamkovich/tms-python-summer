from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey


"""
CREATE TABLE articles(
    id integer,
    title varchar(30),
    description TEXT(256),
    author_name varchar(25)
)
"""

class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)

    """
    CREATE TABLE comments(
        id integer,
        title varchar(30),
        comment TEXT(256),
        author_name varchar(25)
    )
    """

    @property  # свой деф для ограничения выводимых букв
    def short_description(self):
        return self.description[:10]

    def __str__(self):
        return self.title

    def get_image_url(self):
        return f'/media/{self.image}'

# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
#     text = models.CharField(max_length=300)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)
#
#     @property
#     def short_text(self):
#         return self.text[:50]
#
#     def __str__(self):
#         return self.text

class Comment(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(default=None)
    body = models.TextField(default="your comment")
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.article}'



    """
    models.CASCADE
    models.SET_NULL
    models.SET_DEFAULT
    models.DO_NOTHING
    """

