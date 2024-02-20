from django.contrib import admin
from django.urls import path, include
from .views import BlogEventsListAPIView, PublicBlogListAPIView

urlpatterns = [
    path("event-list/", BlogEventsListAPIView.as_view()),
    path("publish/", PublicBlogListAPIView.as_view()),
]
