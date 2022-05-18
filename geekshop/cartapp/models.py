from itertools import product
from pyexpat import model
from django.db import models
from mainapp.models import Product
from django.contrib.auth import get_user_model
# Create your models here.


class CartManager(models.Manager):

    def quantity(self):
        return sum(item.quantity for item in self.all())

    def cost(self):
        return sum(item.product.pice * item.quantity for item in self.all())


class Cart(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CartManager()

    def __str__(self):
        return f'{self.product} - {self.quantity} шт.'
