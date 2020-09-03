from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views import View
from django.contrib import messages

from apps.product.models import Variation
from apps.order.models import Order, ItemOrder
from utils import utils


class OrderPayment(View):
    template_name = 'order/payment.html'

    def get(self, *args, **kwargs):

        if not self.request.session.get('cart'):
            messages.error(
                self.request,
                'Empty cart.'
            )
            return redirect('product:list')

        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Please, login or create account.'
            )
            return redirect('costumer:create')

        cart = self.request.session.get('cart')
        cart_variation_ids = [v for v in cart]

        variations_db = list(
            Variation.objects.select_related('product').filter(id__in=cart_variation_ids)
        )

        for variations in variations_db:
            vid = variations.id
            inventory = variations.inventory
            cart_qt = cart[vid]['quantity']
            price = cart[vid]['price']
            promotional_price = cart[vid]['promotional_price']

            error_msg_inventory = ''

            if inventory < cart_qt:
                cart[vid]['quantity'] = inventory
                cart[vid]['price'] = inventory * price
                cart[vid]['promotional_price'] = inventory * promotional_price
                error_msg_inventory = 'Some products had inventory changes. ' \
                                      'We reduced the quantities in your initial order.'

                if error_msg_inventory:
                    messages.info(
                        self.request,
                        error_msg_inventory,
                    )
                    self.request.save()
                    return redirect('product:cart')

        total_quantity_cart = utils.total_quantity_cart('cart')
        total_value_cart = utils.cart_total('cart')

        order = Order(
            user=self.request.user,
            total=total_value_cart,
            total_quantity=total_quantity_cart,
            status='C',
        )

        order.save()

        ItemOrder.objects.bulk_create(
            [
                ItemOrder(
                    order=order,
                    product=v['product'],
                    product_id=v['product_id'],
                    variation=v['variation_name'],
                    variation_id=v['variation_id'],
                    price=v['quantitative_price'],
                    promotional_price=v['quantitative_promotional_price'],
                    image=v['image'],
                ) for v in cart.values()
            ]
        )

        context = {
            'total_quantity_cart': total_quantity_cart,
            'total_value_cart': total_value_cart,
        }

        del self.request.session['cart']
        #return render(self.request, self.template_name, context)
        return redirect('order:list')


class SaveOrder(View):
    pass


class OrderDetail(ListView):
    pass


class OrderList(ListView):
    pass