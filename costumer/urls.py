from django.urls import path

from .views import CostumerCreation, CostumerUpdate, CostumerLogin, CostumerLogout

app_name = 'costumer'

urlpatterns = [
    path('', CostumerCreation.as_view(), name='create'),
    path('update/', CostumerUpdate.as_view(), name='update'),
    path('login/', CostumerLogin.as_view(), name='login'),
    path('logout/', CostumerLogout.as_view(), name='logout'),
]
