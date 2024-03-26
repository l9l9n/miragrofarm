from django.contrib import admin
from django.urls import path, include
from .views import BlogEventsListAPIView, PublicBlogListAPIView, QuestionsListAPIView, ServiceListAPIView, \
    OurPartnersListAPIView, ContactsListAPIView, ManualVideoListAPIView

urlpatterns = [
    path("event-list/", BlogEventsListAPIView.as_view()),
    path("publish/", PublicBlogListAPIView.as_view()),
    path("questions/", QuestionsListAPIView.as_view()),
    path("service/", ServiceListAPIView.as_view()),
    path("partners/", OurPartnersListAPIView.as_view()),
    path("contact/", ContactsListAPIView.as_view()),
    path("video/", ManualVideoListAPIView.as_view()),
]
