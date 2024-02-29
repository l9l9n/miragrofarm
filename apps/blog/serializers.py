from rest_framework import serializers
<<<<<<< HEAD
from .models import Events, Public, QuestionsAndAnswers
=======

from .models import Events, Public, Questions
>>>>>>> main


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
