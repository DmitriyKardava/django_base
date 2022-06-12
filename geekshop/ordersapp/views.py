from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, UpdateView
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from ordersapp.forms import OrderItemForm
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
    order = get_object_or_404(Order, pk=pk)
    if not order.can_pay:
        return HttpResponseBadRequest
    order.status = Order.PAID
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))


@login_required
def order_cancel(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if not order.can_cancel:
        return HttpResponseBadRequest
    order.status = Order.CANCELED
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    template_name="ordersapp/order_update.html"
    model = Order
    success_url = reverse_lazy("orders:list")
    title = "Редактирование заказа"
    fields = ()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderItemFormset = inlineformset_factory(Order, OrderItem, OrderItemForm, extra=1)
        formset = OrderItemFormset(instance=self.object)
        context['orderitems'] = formset
        context['title'] = "Редактирование заказа"
        return context
    
    def form_valid(self, form):
        OrderItemFormset = inlineformset_factory(Order, OrderItem, OrderItemForm, extra=1)
        formset = OrderItemFormset(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()

        return super().form_valid(form)
