from .apiviews import ProductAPIViewSet, VariationAPIViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('product', ProductAPIViewSet)
router.register('variations', VariationAPIViewSet)