from rest_framework import serializers
from .models import Events, Public, QuestionsAndAnswers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = '__all__'


class QuestionsAndAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsAndAnswers
        fields = '__all__'
