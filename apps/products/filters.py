from django_filters import rest_framework as filters
from apps.products.models import Product


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    applying = filters.CharFilter(field_name='applying', lookup_expr='icontains')
    sub_category = filters.CharFilter(field_name='sub_category__slug', lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['applying', 'sub_category']
