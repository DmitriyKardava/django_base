from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from cartapp.models import Cart
from mainapp.models import Product

# Create your views here.
from django.urls import path


def view(request):
    return render(request, 'cartapp/view.html', context={
        'title': 'Корзина'
    })


def add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.filter(user=request.user, product=product).first()
    if not cart:
        cart = Cart(user=request.user, product=product)
    cart.quantity += 1
    cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('index')))


def remove(request, cart_id):
    cart = get_object_or_404(Cart, pk=cart_id)
    cart.delete()
    return HttpResponseRedirect(reverse('cart:view'))
