from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 9


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class AddToCart(View):
    pass


class RemoveFromCart(View):
    pass


class Cart(View):
    pass


class Conclude(View):
    pass
