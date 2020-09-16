from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def short_description(self):
        return self.description[:5]

    def __str__(self):
        return self.title