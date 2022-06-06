from atexit import register
from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='cart_folder')
def cart_folder(string):
    if not string:
        string = 'cart_images/default.jpg' 
    return f'{settings.MEDIA_URL}{string}'

