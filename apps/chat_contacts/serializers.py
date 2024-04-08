from rest_framework import serializers
from models import ChatContacts


class ChatContactsSerializer(serializers.Serializer):
    class Meta:
        model = ChatContacts
        fields = 'chat_link'
