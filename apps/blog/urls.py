from django.contrib import admin
from django.urls import path, include
from .views import BlogEventsListAPIView, PublicBlogListAPIView

urlpatterns = [
    path("blog-event-list/", BlogEventsListAPIView.as_view()),
    path("blog_pub/", PublicBlogListAPIView.as_view()),
]
