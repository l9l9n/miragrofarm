from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .filters import ProductFilter
from .models import Product, Order, Subscription
from rest_framework import generics
from .serializers import ProductDetailSerializer, OrderSerializer, ProductListSerializer, SubscriptionSerializer
from rest_framework.permissions import  AllowAny

from .signals import send_subscription_email


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = ProductFilter
    ordering_fields = ('name',)
    search_fields = ('name',)
    search_fields = ['name', 'slug_name']

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
