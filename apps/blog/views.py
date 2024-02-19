from django.shortcuts import render
from rest_framework import generics

from .models import Events, Public
from .serializer import EventSerializer, PublicSerializer


class BlogEventsListAPIView(generics.ListAPIView):

    queryset = Events.objects.all()
    serializer_class = EventSerializer


class PublicBlogListAPIView(generics.ListAPIView):

    queryset = Public.objects.all()
    serializer_class = PublicSerializer

