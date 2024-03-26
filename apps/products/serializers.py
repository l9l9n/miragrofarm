from rest_framework import serializers
from .models import Product, Order, Subscription, IconAnimal, FilePDF


class IconAnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = IconAnimal
        fields = ['id', 'name', 'icon']


class FilePDFSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilePDF
        fields = ['name', 'pdf_file']


class ProductListSerializer(serializers.ModelSerializer):
    icon_animal = IconAnimalSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug_name', 'img_product', 'short_description', 'icon_animal',)


class ProductDetailSerializer(serializers.ModelSerializer):
    icon_animal = IconAnimalSerializer(many=True, read_only=True)
    pdf_file = FilePDFSerializer(many=True, read_only=True)
    """Сериализатор для продуктов"""
    class Meta:
        model = Product
        fields = (
            'name',
            'slug_name',
            'img_product',
            'short_description',
            'icon_animal',
            'description',
            'compound',
            'applying',
            'waiting_time',
            'release_form',
            'storage_date',
            'storage_conditions',
            'sub_category',
            'is_new_product',
            'pdf_file',
        )


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

