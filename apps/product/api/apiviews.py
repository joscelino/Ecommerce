from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from apps.product.models import Product, Variation
from apps.product.api.api_permissions import IsSuperUser
from apps.product.api.serializers import ProductSerializer, VariationSerializer


class ProductAPIViewSet(viewsets.ModelViewSet):
    """ Product API """
    permission_classes = (
        IsSuperUser,
        permissions.DjangoModelPermissions,
    )
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
    permission_classes = (
        IsSuperUser,
        permissions.DjangoModelPermissions,
    )

    queryset = Variation.objects.all()
    serializer_class = VariationSerializer


