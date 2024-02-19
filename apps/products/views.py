from rest_framework.response import Response

from .models import Product, Order
from rest_framework import generics, viewsets
from rest_framework import mixins
from .serializer import ProductDetailSerializer, OrderSerializer, ProductListSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name',]


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'


class OrderViewSet(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
