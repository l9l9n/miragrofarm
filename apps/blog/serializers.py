from rest_framework import serializers
from .models import Events, Public, Questions, Service, OurPartners, OwnerContacts, ManualVideo, ExhibitionCalendar


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'title', 'short_description', 'created_at', 'image',)


class EventDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ('id', 'title', 'description', 'created_at', 'image',)


class PublicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = ('id', 'title', 'short_description', 'created_at', 'image',)


class PublicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = ('id', 'title', 'description', 'created_at', 'image',)


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'name', 'description', 'image',)


class OurPartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = OurPartners
        fields = ('id', 'img_partner',)


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OwnerContacts
        fields = ('id', 'owner', 'company', 'phone', 'email', 'address',)


class ManualVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ManualVideo
        fields = ('id', 'name', 'description', 'img_preview', 'link', 'created',)


class ExhibitionCalendarSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExhibitionCalendar
        fields = ('id', 'name_exhibition', 'period', 'data_of_participation', 'location',)
