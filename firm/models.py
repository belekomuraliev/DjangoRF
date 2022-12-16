from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование товара')
    price = models.FloatField(verbose_name='Цена товара')
    firm = models.ForeignKey('Firm', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Firm(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название Фирмы')
    address = models.CharField(max_length=50, verbose_name='Адрес Фирмы')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название категории')

    def __str__(self):
        return self.name

