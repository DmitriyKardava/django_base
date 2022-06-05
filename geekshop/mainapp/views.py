import json
import random
from pathlib import Path
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from geekshop.settings import BASE_DIR
from django.core.paginator import Paginator
from .models import Category, Product

with open(BASE_DIR / 'mainapp' / 'data' / 'main_menu.json', 'r',
          encoding='utf-8') as f:
    main_menu = json.load(f)


# Create your views here.

# TODO: Создать view из main_menu.json

def index(request):
    return render(request, Path('mainapp', 'index.html'),
                  context={'menu': main_menu})


def products(request, page=1):
    categories = Category.objects.all()
    products = Product.objects.all()
    hot_product = random.choice(products)
    products = products.exclude(pk=hot_product.pk)
    paginator = Paginator(products, per_page=3)
    if page > paginator.num_pages:
        return HttpResponseRedirect(reverse('products'))
    return render(request, Path('mainapp', 'products.html'),
                  context={
                      'title': 'Продукты',
                      'menu': main_menu,
                      'categories': categories,
                      'products': paginator.page(page),
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


def category(request, pk, page=1):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category).order_by('price')
    paginator = Paginator(products, per_page=3)
    if page > paginator.num_pages:
        return HttpResponseRedirect(reverse('category', args=[category.id]))
    return render(request, Path('mainapp', 'category.html'),
                  context={
        'title': 'Продукты',
        'menu': main_menu,
        'category': category,
        'categories': categories,
        'products': paginator.page(page)
    }
    )


def contact(request):
    return render(request, Path('mainapp', 'contact.html'),
                  context={'menu': main_menu})
