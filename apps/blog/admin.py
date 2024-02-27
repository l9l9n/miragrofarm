from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(Events)
class BlogEventsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'created_at',
        'image',
        'slug'
    ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Public)
class BlogPublicAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'created_at',
        'image',
        'slug'
    ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(NewProducts)
class BlogNewProductsAdmin(admin.ModelAdmin):
    list_display = [
        'product_name',
        'slug'
    ]
    prepopulated_fields = {'slug': ('product_name',)}


@admin.register(ExhibitionCalendar)
class BlogCalendarAdmin(admin.ModelAdmin):
    list_display = [
        'name_exhibition',
        'period',
        'data_of_participation',
        'location',
        'slug'
    ]
    prepopulated_fields = {'slug': ('name_exhibition',)}


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'questions'
    ]
    def has_add_permission(self, request):
        return False
