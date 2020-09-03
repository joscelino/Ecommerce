from django.urls import path

from .views import OrderPayment, OrderDetail, SaveOrder, OrderList


app_name = 'order'

urlpatterns = [
    path('payment/<int:pk>', OrderPayment.as_view(), name='payment'),
    path('save_order/', SaveOrder.as_view(), name='save_order'),
    path('detail/', OrderDetail.as_view(), name='detail'),
    path('list/', OrderList.as_view(), name='list'),
]
