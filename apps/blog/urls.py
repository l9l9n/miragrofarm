from django.urls import path
from .views import (EventsListAPIView, PublicListAPIView, QuestionsListAPIView, \
                    ServiceListAPIView, OurPartnersListAPIView, ContactsListAPIView, \
                    ManualVideoListAPIView, ExhibitionCalendarListAPIView, EventDetailRetrieveAPIView,
                    PublicDetailRetrieveAPIView
                    )

urlpatterns = [
    path("event/", EventsListAPIView.as_view()),
    path("event/<int:pk>/", EventDetailRetrieveAPIView.as_view()),
    path("publish/", PublicListAPIView.as_view()),
    path("publish/<int:pk>/", PublicDetailRetrieveAPIView.as_view()),
    path("calendar/", ExhibitionCalendarListAPIView.as_view()),
    path("questions/", QuestionsListAPIView.as_view()),
    path("service/", ServiceListAPIView.as_view()),
    path("partners/", OurPartnersListAPIView.as_view()),
    path("contact/", ContactsListAPIView.as_view()),
    path("video/", ManualVideoListAPIView.as_view()),
]
