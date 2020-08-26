from django.urls import path
from rest_framework.routers import SimpleRouter

from .apiviews import ProductAPIViewSet, VariationAPIViewSet

router = SimpleRouter()
router.register('product', ProductAPIViewSet)
router.register('variations', VariationAPIViewSet)

