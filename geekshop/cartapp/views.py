from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string 
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cartapp.models import Cart
from mainapp.models import Product

# Create your views here.
from django.urls import path


@login_required
def view(request):
    return render(request, 'cartapp/view.html', context={
        'title': 'Корзина'
    }
    )


@login_required
def add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.filter(user=request.user, product=product).first()
    if not cart:
        cart = Cart(user=request.user, product=product)
    cart.quantity += 1
    cart.save()

    if 'next' in request.META.get('HTTP_REFERER'):
        redirect_url = reverse('index')
    else:
        redirect_url = request.META.get('HTTP_REFERER', reverse('index'))
    return HttpResponseRedirect(redirect_url)


@login_required
def remove(request, cart_id):
    cart = get_object_or_404(Cart, pk=cart_id)
    cart.delete()
    return HttpResponseRedirect(reverse('cart:view'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_cart_item = Cart.objects.get(pk=int(pk))

    if quantity > 0:
        new_cart_item.quantity = quantity 
        new_cart_item.save()
    else:
        new_cart_item.delete()

    cart_items = Cart.objects.filter(user=request.user).order_by('product__category')
    content = {
        'cart_items': cart_items,
    }
    result = render_to_string('cartapp/includes/inc_basket_list.html', content)
    return JsonResponse({'result': result})
