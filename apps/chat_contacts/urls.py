from django.urls import path
from .views import ChatContactListAPIView

urlpatterns = [
    path("choice_chat/", ChatContactListAPIView.as_view()),
]
