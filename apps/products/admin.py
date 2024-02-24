from django.contrib import admin
from .models import Product, SubCategory, Category, Order, IconAnimal, Subscription


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "short_description",
        "get_type_animals",
        "compound",
        'get_truncated_description',
        'applying',
        'waiting_time',
        'release_form',
        'storage_date',
        'storage_conditions',
        'sub_category',
        'id',
    ]

    def get_type_animals(self, obj):
        return ", ".join([animal.name for animal in obj.icon_animal.all()])
    get_type_animals.short_description = "Типы животных"

    def get_truncated_description(self, obj):
        return obj.description[:50] + '...' if obj.description and len(obj.description) > 30 else obj.description
    get_truncated_description.short_description = "Описание"


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'category'
    ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
    ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'email',
    ]


@admin.register(IconAnimal)
class IconAnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'icon']
    ordering = ['name']


@admin.register(Subscription)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email']
