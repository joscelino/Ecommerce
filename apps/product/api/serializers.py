from rest_framework import serializers

from apps.product.models import Product, Variation


class VariationSerializer(serializers.ModelSerializer):
    model = Variation
    fields = (
        'product',
        'name',
        'price',
        'promotional_price',
        'inventory',
    )


class ProductSerializer(serializers.ModelSerializer):
    """ Rest API Serializer """
    variations = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail',
    )

    class Meta:
        extra_kwargs = {
            'image': {'write_only': True},
            'pk': {'read_only': True},
        }

        model = Product
        fields = (
            'name',
            'short_description',
            'long_description',
            'slug',
            'price',
            'promotional_price',
            'product_type',
            'active',
            'variations',
        )
