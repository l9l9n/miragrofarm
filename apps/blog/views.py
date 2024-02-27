from django.shortcuts import render
from rest_framework import generics

from .models import Events, Public, Questions
from .serializers import EventSerializer, PublicSerializer, QuestionsSerializer


class BlogEventsListAPIView(generics.ListAPIView):

    queryset = Events.objects.all()
    serializer_class = EventSerializer


class PublicBlogListAPIView(generics.ListAPIView):

    queryset = Public.objects.all()
    serializer_class = PublicSerializer


class QuestionsListAPIView(generics.CreateAPIView):

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
