from django import template

register = template.Library()


@register.simple_tag
def disabled_if_cannot_buy(product, user):
    if product.quantity == 0:
        return 'disabled'

    cart_item = user.cart.filter(product=product).first()
    if cart_item and cart_item.quantity + 1 > product.quantity:
        return 'disabled'
    
    return ''
