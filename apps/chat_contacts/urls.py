from django.urls import path
from .views import ChatContactListAPIView

urlpatterns = [
    path("chat/", ChatContactListAPIView.as_view()),
]
