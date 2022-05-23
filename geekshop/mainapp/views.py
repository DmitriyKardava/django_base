import json
import random
from pathlib import Path
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from geekshop.settings import BASE_DIR
from .models import Category, Product

with open(BASE_DIR / 'mainapp' / 'data' / 'main_menu.json', 'r',
          encoding='utf-8') as f:
    main_menu = json.load(f)


# Create your views here.

# TODO: Создать view из main_menu.json

def index(request):
    return render(request, Path('mainapp', 'index.html'),
                  context={'menu': main_menu})


def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    hot_product = random.choice(products)
    products = products.exclude(pk=hot_product.pk)[:3]
    return render(request, Path('mainapp', 'products.html'),
                  context={
                      'title': 'Продукты',
                      'menu': main_menu,
                      'categories': categories,
                      'products': products,
                      'hot_product': hot_product
    }
    )


def product(request, pk):
    categories = Category.objects.all()
    product = get_object_or_404(Product, pk=pk)
    return render(request, Path('mainapp', 'product.html'),
                  context={
                      'title': product.name,
                      'menu': main_menu,
                      'categories': categories,
                      'category': product.category,
                      'product': product
    }
    )


def category(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category)

    return render(request, Path('mainapp', 'category.html'),
                  context={
        'title': 'Продукты',
        'menu': main_menu,
        'category': category,
        'categories': categories,
        'products': products
    }
    )


def contact(request):
    return render(request, Path('mainapp', 'contact.html'),
                  context={'menu': main_menu})
