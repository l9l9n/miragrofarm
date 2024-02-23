from rest_framework import serializers
from .models import Product, Order, Subscription, IconAnimal


class IconAnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = IconAnimal
        fields = ['id', 'name', 'icon']


class ProductListSerializer(serializers.ModelSerializer):
    icon_animal = IconAnimalSerializer(many=True, read_only=True)

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


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['email']

    def validate_email(self, value):
        return value

