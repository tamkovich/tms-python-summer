from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



"""
CREATE TABLE articles(
    id integer,
    title varchar(30),
    description TEXT(256),
    author_name varchar(25)
)
"""

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)
    published = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='category_article')
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

    def get_absolute_url(self):
        return reverse('article_edit', kwargs={'pk': self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='comments_article',
                                verbose_name='article',
                                blank=True,
                                null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                               verbose_name='author', blank=True)
    text = models.TextField(default=None, verbose_name='add comment')
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, verbose_name='looking article')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.author} on {self.article}'

    @property  # свой деф для ограничения выводимых букв
    def short_text(self):
        return self.text[:10]

    """
    models.CASCADE
    models.SET_NULL
    models.SET_DEFAULT
    models.DO_NOTHING
    """



