from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена')
    quantity = models.IntegerField('Количество')
    comment = models.CharField('Комментарий', max_length=255)

    @staticmethod
    def get_absolute_url():
        return reverse('index')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
