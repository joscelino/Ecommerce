from django.template import Library
from utils import utils

register = Library()


@register.filter
def price_formatted(val) -> str:
    return utils.price_formatted(val)


@register.filter
def total_quantity_cart(cart) -> int:
    return utils.total_quantity_cart(cart)


@register.filter
def cart_total(cart):
    return utils.cart_total(cart)
