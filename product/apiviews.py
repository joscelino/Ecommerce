from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product, Variation
from .serializers import ProductSerializer, VariationSerializer


class ProductAPIViewSet(viewsets.ModelViewSet):
    """ Product API """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'])
    def variations(self, request, pk=None):
        product = self.get_object()
        serializer = VariationSerializer(product.variations.all(), many=True)
        return Response(serializer.data)


class VariationAPIViewSet(viewsets.ModelViewSet):
    """ Variation product API """
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer

# TODO: Insert routes in urls
