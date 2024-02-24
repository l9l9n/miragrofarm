from django.shortcuts import render
from rest_framework import generics

from .models import Events, Public, QuestionsAndAnswers
from .serializers import EventSerializer, PublicSerializer, QuestionsAndAnswersSerializer


class BlogEventsListAPIView(generics.ListAPIView):

    queryset = Events.objects.all()
    serializer_class = EventSerializer


class PublicBlogListAPIView(generics.ListAPIView):

    queryset = Public.objects.all()
    serializer_class = PublicSerializer


class QuestionsAndAnswersListAPIView(generics.ListAPIView):

    queryset = QuestionsAndAnswers.objects.all()
    serializer_class = QuestionsAndAnswersSerializer
