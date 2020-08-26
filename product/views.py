from django.views.generic.list import ListView
from django.views import View
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 9


class ProductDetail(View):
    pass


class AddToCart(View):
    pass


class RemoveFromCart(View):
    pass


class Cart(View):
    pass


class Conclude(View):
    pass
