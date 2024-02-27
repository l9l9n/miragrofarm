from django.contrib import admin
from django.urls import path, include
from .views import BlogEventsListAPIView, PublicBlogListAPIView, QuestionsListAPIView

urlpatterns = [
    path("event-list/", BlogEventsListAPIView.as_view()),
    path("publish/", PublicBlogListAPIView.as_view()),
    path("questions/", QuestionsListAPIView.as_view()),
]
