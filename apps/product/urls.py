from django.urls import path
from rest_framework.routers import SimpleRouter

from .apiviews import ProductAPIViewSet, VariationAPIViewSet
from .views import ProductList, ProductDetail, AddToCart, RemoveFromCart, Cart, Conclude

router = SimpleRouter()
router.register('product', ProductAPIViewSet)
router.register('variations', VariationAPIViewSet)

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<slug>', ProductDetail.as_view(), name='detail'),
    path('addtocart/', AddToCart.as_view(), name='addtocart'),
    path('removefromcart/', RemoveFromCart.as_view(), name='removefromcart'),
    path('cart/', Cart.as_view(), name='cart'),
    path('conclude/', Conclude.as_view(), name='conclude'),
]
