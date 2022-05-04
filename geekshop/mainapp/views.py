import json
from pathlib import Path
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from geekshop.settings import BASE_DIR
from .models import Category, Product

with open(BASE_DIR / 'mainapp' / 'data' / 'main_menu.json') as f:
    main_menu = json.load(f)


# Create your views here.

# TODO: Создать view из main_menu.json

def index(request):
    return render(request, Path('mainapp', 'index.html'),
                  context={'menu': main_menu})


def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, Path('mainapp', 'products.html'),
                  context={
                      'title': 'Продукты',
                      'menu': main_menu,
                      'categories': categories,
                      'products': products
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
