from rest_framework import serializers

from product_service.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer."""
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Order serializer."""
    class Meta:
        model = Order
        fields = '__all__'
