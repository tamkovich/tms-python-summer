from django.db import models
from django.contrib.auth.models import User


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

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def short_comment(self):
        return self.comment[:50]

    def __str__(self):
        return self.comment

    """
    models.CASCADE
    models.SET_NULL
    models.SET_DEFAULT
    models.DO_NOTHING
    """

