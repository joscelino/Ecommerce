from rest_framework import generics

from .models import Product, Variation
from .serializers import ProductSerializer, VariationSerializers


class ProductsAPIView(generics.ListCreateAPIView):
    """ Product API  - List and create """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Product API - Update """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class VariationsAPIView(generics.ListCreateAPIView):
    """ Variation product API - List and create """
    queryset = Variation.objects.all()
    serializer_class = VariationSerializers


class VariationAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Variation product API - Update """
    queryset = Variation.objects.all()
    serializer_class = VariationSerializers

# TODO: Insert routes in urls
