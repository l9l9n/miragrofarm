from rest_framework import serializers
from .models import Product, Order


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'short_description', 'icon_animal',)


class ProductDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для продуктов"""
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для заказов"""
    class Meta:
        model = Order
        fields = ('id', 'name', 'phone', 'email', 'date')
