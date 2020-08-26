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
        """ Displays product variations and pagination, if possible """
        self.pagination_class.page_size = 5
        variations = Variation.objects.filter(product_id=pk)
        page = self.paginate_queryset(variations)

        if page is not None:
            serializer = VariationSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = VariationSerializer(variations, many=True)
        return Response(serializer.data)


class VariationAPIViewSet(viewsets.ModelViewSet):
    """ Variation product API """
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer


