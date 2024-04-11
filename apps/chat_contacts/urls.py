from django.urls import path
from .views import ChatContactListAPIView

urlpatterns = [
    path("chats/", ChatContactListAPIView.as_view()),
]
