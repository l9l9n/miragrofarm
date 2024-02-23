from .models import Product, Order, Subscription, IconAnimal
from rest_framework import generics, viewsets
from rest_framework import mixins
from .serializer import ProductDetailSerializer, OrderSerializer, ProductListSerializer, SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

from .signals import send_subscription_email
from django.http import HttpResponse


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name',]

    def get_queryset(self):
        queryset = Product.objects.all()
        icon_id = self.kwargs.get('icon_id')
        if icon_id is not None:
            queryset = queryset.filter(icon_animal__id=icon_id)
        return queryset


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Product.objects.all()
        icon_id = self.kwargs.get('icon_id')
        if icon_id is not None:
            queryset = queryset.filter(icon_animal__id=icon_id)
        return queryset


class OrderViewSet(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SubscribeAPIView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_subscription_email(instance.email)


class NewProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Product.objects.filter(is_new_product=True)
        icon_id = self.kwargs.get('icon_id')
        if icon_id is not None:
            queryset = queryset.filter(icon_animal__id=icon_id)
        return queryset
