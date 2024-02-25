from django_filters import rest_framework as filters
from apps.products.models import Product


class ProductFilter(filters.FilterSet):
    applying = filters.CharFilter(field_name='applying', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['applying']
