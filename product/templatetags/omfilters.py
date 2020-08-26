from django.template import Library
from utils import utils

register = Library()


@register.filter
def price_formatted(val) -> str:
    return utils.price_formatted(val)
