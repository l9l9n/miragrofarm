from rest_framework import serializers
from .models import ChatContacts


class ChatContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatContacts
        fields = ('id', 'chat_link',)
