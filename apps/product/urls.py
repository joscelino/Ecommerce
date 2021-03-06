from django.urls import path

from .views import (
    ProductList,
    ProductDetail,
    AddToCart,
    RemoveFromCart,
    Cart,
    Checkout,
    Search,
)


app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<slug>', ProductDetail.as_view(), name='detail'),
    path('addtocart/', AddToCart.as_view(), name='addtocart'),
    path('removefromcart/', RemoveFromCart.as_view(), name='removefromcart'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('search/', Search.as_view(), name='search'),
]

