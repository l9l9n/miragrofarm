from django.urls import path, include
from .views import ProductListAPIView, ProductDetailAPIView, OrderViewSet, SubscribeAPIView, NewProductListAPIView

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="list"),
    path("<int:pk>/", ProductDetailAPIView.as_view(), name="detail"),
    path("new/", NewProductListAPIView.as_view(), name="new-product"),
    path("order/", OrderViewSet.as_view(), name="order"),
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe')
]
