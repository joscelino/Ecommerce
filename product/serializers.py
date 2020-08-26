from rest_framework import serializers

from .models import Product, Variation


class ProductSerializer(serializers.ModelSerializer):
    """ Rest API Serializer """
    class Meta:
        extra_kargs = {
            'image': {'write_only': True}
        }

        model = Product
        fields = (
            'pk',
            'name',
            'short_description',
            'long_description',
            'slug',
            'price',
            'promotional_price',
            'product_type',
            'active',
        )


class VariationSerializer(serializers.ModelSerializer):
    model = Variation
    fields = (
        'product',
        'name',
        'price',
        'promotional_price',
        'inventory',
    )