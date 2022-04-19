from pathlib import Path
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, Path('mainapp', 'index.html'))


def products(request):
    return render(request, Path('mainapp', 'products.html'))


def contact(request):
    return render(request, Path('mainapp', 'contact.html'))
