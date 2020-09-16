from django.db import models
from django.urls import reverse


class Books(models.Model):
    title = models.CharField('Название', max_length=50)
    author_name = models.CharField('Имя автора', max_length=50)
    description = models.TextField('Описание')

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.id])

    @property
    def short_description(self):
        return self.description[:10]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
