from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib import messages


from .models import Product, Variation


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 9
    ordering = ['-pk']


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class AddToCart(View):

    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list')
        )
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            messages.error(
                self.request,
                'Product not found',
            )
            return redirect(http_referer)

        variation = get_object_or_404(Variation, id=variation_id)
        inventory_variation = variation.inventory
        product = variation.product
        product_id = product.pk
        product_name = product.name
        variation_name = variation.name or ''
        price = variation.price
        promotional_price = variation.promotional_price
        quantity = 1
        slug = product.slug
        image = product.image

        if image:
            image = image.name
        else:
            image = ''

        if variation.inventory < 1:
            messages.error(
                self.request,
                'Unavailable',
            )
            return redirect(http_referer)

        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()

        cart = self.request.session['cart']

        if variation_id in cart:
            cart_quantity = cart[variation_id]['quantity']
            cart_quantity += 1

            if inventory_variation < cart_quantity:
                messages.warning(
                    self.request,
                    f'There is no {cart_quantity} units for {product_name}. Added {inventory_variation} in the cart.'
                )
                cart_quantity = inventory_variation

            cart[variation_id]['quantity'] = cart_quantity
            cart[variation_id]['quantitative_price'] = price * cart_quantity
            cart[variation_id]['quantitative_promotional_price'] = promotional_price * cart_quantity

        else:
            cart[variation_id] = {
                'product': product,
                'product_id': product_id,
                'product_name': product_name,
                'variation_name': variation_name,
                'variation_id': variation_id,
                'quantitative_price': price,
                'quantitative_promotional_price': promotional_price,
                'quantity': 1,
                'slug': slug,
                'image': image,
            }

        self.request.session.save()
        messages.success(
            self.request,
            f'Product: {product_name} added in the cart with success'
        )
        return redirect(http_referer)


class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list')
        )
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            return redirect(http_referer)

        if not self.request.session.get('cart'):
            return redirect(http_referer)

        if variation_id not in self.request.session['cart']:
            return redirect(http_referer)

        cart = self.request.session['cart'][variation_id]

        messages.success(
            self.request,
            f'Product {cart["product_name"]} {cart["variation_name"]} was removed from your cart.'
        )

        del self.request.session['cart'][variation_id]
        self.request.session.save()

        return redirect(http_referer)


class Cart(View):

    def get(self, *args, **kwargs):
        context = {
            'cart': self.request.session.get('cart', {}),
        }
        return render(self.request, 'product/cart.html', context)


class Checkout(View):
    pass
