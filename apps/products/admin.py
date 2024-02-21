from django.contrib import admin
from .models import Product, SubCategory, Category, Order, IconAnimal


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "short_description",
        "icon_animal",
        "compound",
        'description',
        'applying',
        'waiting_time',
        'release_form',
        'storage_date',
        'storage_conditions',
        'sub_category',
        'id',
    ]

    def icon_animal(self, obj):
        return ", ".join([icon.name for icon in obj.icons.all()])
    icon_animal.short_description = "Иконка"


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
