from django.db import models

class Item(models.Model):
    """Класс товар"""
    title = models.CharField('Название', max_length=30)
    price = models.IntegerField('Цена', default=0)

    def __str__(self):
        return f'{self.id})Товар {self.title} стоит {self.price} руб.'

# Create your models here.
