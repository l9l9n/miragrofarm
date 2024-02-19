from django.urls import path, include
from .views import ProductListAPIView, ProductDetailAPIView, OrderViewSet

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="list"),
    path("<int:pk>/", ProductDetailAPIView.as_view(), name="detail"),
    path("order/", OrderViewSet.as_view(), name="order"),
]
