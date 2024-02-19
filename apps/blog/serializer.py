from rest_framework import serializers
from .models import Events, Public, NewProducts


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = '__all__'


class NewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProducts
        fields = '__all__'
