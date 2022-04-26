import json
from pathlib import Path
from django.shortcuts import render
from geekshop.settings import BASE_DIR


with open(BASE_DIR / 'mainapp' / 'data' / 'main_menu.json') as f:
    main_menu = json.load(f)


# Create your views here.

# TODO: Создать view из main_menu.json  

def index(request):
    return render(request, Path('mainapp', 'index.html'), 
        context={'menu': main_menu})


def products(request):
    return render(request, Path('mainapp', 'products.html'), 
        context={'menu': main_menu})


def contact(request):
    return render(request, Path('mainapp', 'contact.html'), 
        context={'menu': main_menu})
