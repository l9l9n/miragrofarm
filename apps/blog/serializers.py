from rest_framework import serializers
from .models import Events, Public, Questions, Service


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'name', 'email', 'phone', 'questions', 'date')

