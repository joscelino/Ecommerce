from django.urls import path

from .views import OrderPayment, OrderDetail, OrderConclude


app_name = 'order'

urlpatterns = [
    path('', OrderPayment.as_view(), name='payment'),
    path('conclude/', OrderConclude.as_view(), name='conclude'),
    path('detail/', OrderDetail.as_view(), name='detail'),
]
