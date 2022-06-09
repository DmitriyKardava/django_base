from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import get_object_or_404 
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from utils.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from django.db import transaction

class OrderList(LoginRequiredMixin, ListView):
    # template_name = 'ordersapp/order_list.html'
    model: Order
    title = 'Заказы'

    def get_queryset(self):
        return Order.objects.order_by('created_at')


@login_required
@transaction.atomic
def create_order(request):
    cart_items = request.user.cart.all()
    if not cart_items:
        return HttpResponseBadRequest()

    order = Order(user=request.user)
    order.save()
    for item in cart_items:
        order_item = OrderItem(
            order=order, product=item.product, quantity=item.quantity)
        order_item.save()

    cart_items.delete()
    return HttpResponseRedirect(reverse('orders:list'))

@login_required
def order_pay(request, pk):
    order = get_object_or_404(pk=pk)
    if not order.can_pay :
        return HttpResponseBadRequest
    order.status = Order.PAID
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))

@login_required
def order_cancel(request, pk):
    order = get_object_or_404(pk=pk)
    if not order.can_cancel :
        return HttpResponseBadRequest
    order.status = Order.CANCEL
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))

    