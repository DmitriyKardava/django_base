from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=128, blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self) -> str:
        return f'{self.id}: {self.name}'


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=128, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products')
    is_active = models.BooleanField(verbose_name='активный', default=True)

    def __str__(self) -> str:
        return f'{self.id}: {self.name}'
