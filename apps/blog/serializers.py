from rest_framework import serializers
from .models import Events, Public, Questions, Service, OurPartners, Contacts, ManualVideo


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
        fields = ('id', 'name', 'email', 'phone', 'questions', 'date',)


class OurPartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = OurPartners
        fields = ('id', 'img_partner',)


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = ('id', 'owner', 'company', 'phone', 'email', 'address',)


class ManualVideoSerializer(serializers.Serializer):

    class Meta:
        model = ManualVideo
        fields = ('id', 'name', 'description', 'img_preview', 'link', 'created',)
