from django.contrib import admin
from .models import Product, SubCategory, Category, Order, IconAnimal, Subscription, FilePDF


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "short_description",
        "get_type_animals",
        "get_truncated_compound",
        'get_truncated_description',
        'get_truncated_applying',
        'get_truncated_waiting_time',
        'get_truncated_release_form',
        'get_truncated_storage_date',
        'get_truncated_storage_conditions',
        'sub_category',
        'get_pdf_file',
        'id',
    ]

    prepopulated_fields = {'slug_name': ('name',)}

    fieldsets = [
        ('Русский основной', {'fields': [
            'name',
            'slug_name',
            "img_product",
            "icon_animal",
            'sub_category',
            'is_new_product',
            'pdf_file',
            'short_description',
            'compound',
            'description',
            'applying',
            'waiting_time',
            'release_form',
            'storage_date',
            'storage_conditions',

        ]}),
        ('Кыргызский перевод', {'fields': [
            'short_description_kg',
            'compound_kg',
            'description_kg',
            'applying_kg',
            'waiting_time_kg',
            'release_form_kg',
            'storage_date_kg',
            'storage_conditions_kg',
            # 'sub_category_kg',
        ]}),
    ]

    def get_type_animals(self, obj):
        return ", ".join([animal.name for animal in obj.icon_animal.all()])
    get_type_animals.short_description = "Типы животных"

    def get_pdf_file(self, obj):
        return ", ".join([file.name for file in obj.pdf_file.all()])
    get_pdf_file.short_description = "PDF файлы"

    def get_truncated_compound(self, obj):
        return obj.applying[:30] + '...' if obj.applying and len(obj.applying) > 30 else obj.applying
    get_truncated_compound.short_description = "Состав"

    def get_truncated_description(self, obj):
        return obj.description[:50] + '...' if obj.description and len(obj.description) > 30 else obj.description
    get_truncated_description.short_description = "Описание"

    def get_truncated_applying(self, obj):
        return obj.applying[:30] + '...' if obj.applying and len(obj.applying) > 30 else obj.applying
    get_truncated_applying.short_description = "Применение"

    def get_truncated_waiting_time(self, obj):
        return obj.applying[:30] + '...' if obj.applying and len(obj.applying) > 30 else obj.applying
    get_truncated_waiting_time.short_description = "Период ожидания"

    def get_truncated_release_form(self, obj):
        return obj.applying[:30] + '...' if obj.applying and len(obj.applying) > 30 else obj.applying
    get_truncated_release_form.short_description = "Форма выпуска"

    def get_truncated_storage_date(self, obj):
        return obj.applying[:30] + '...' if obj.applying and len(obj.applying) > 30 else obj.applying
    get_truncated_storage_date.short_description = "Условия хранения"

    def get_truncated_storage_conditions(self, obj):
        return obj.applying[:30] + '...' if obj.applying and len(obj.applying) > 30 else obj.applying
    get_truncated_storage_conditions.short_description = "Срок хранения"


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'category'
    ]
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = [
        ('Русский основной', {'fields': ['name', 'category', 'slug',]}),
        ('Кыргызский перевод', {'fields': ['name_kg', 'category_kg',]})
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
    ]
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = [
        ('Русский основной', {'fields': ['name', 'slug',]}),
        ('Кыргызский перевод', {'fields': ['name_kg',]})
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'email',
    ]

    fieldsets = [
        ('Русский основной', {'fields': ['name', 'phone', 'email',]}),
        ('Кыргызский перевод', {'fields': ['name_kg', 'phone_kg', 'email_kg']})
    ]

    def has_add_permission(self, request):
        return False


@admin.register(IconAnimal)
class IconAnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'icon']
    ordering = ['name']


@admin.register(Subscription)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email']

    fieldsets = [
        ('Русский основной', {'fields': ['email',]}),
        ('Кыргызский перевод', {'fields': ['email_kg']})
    ]

    def has_add_permission(self, request):
        return False


@admin.register(FilePDF)
class FilePDFAdmin(admin.ModelAdmin):
    list_display = ['name']
