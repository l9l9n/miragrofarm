from rest_framework import generics
from .models import ChatContacts
from .serializers import ChatContactsSerializer


class ChatContactListAPIView(generics.ListAPIView):
    queryset = ChatContacts.objects.all()
    serializer_class = ChatContactsSerializer
