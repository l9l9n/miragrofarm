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

    fieldsets = [
        ('Русский основной', {'fields': ['title', 'description', 'slug',]}),
        ('Кыргызский перевод', {'fields': ['title_kg', 'description_kg']})
    ]


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

    fieldsets = [
        ('Русский основной', {'fields': ['title', 'description', 'slug',]}),
        ('Кыргызский перевод', {'fields': ['title_kg', 'description_kg']})
    ]


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

    fieldsets = [
        ('Русский основной', {'fields': ['name_exhibition', 'period', 'data_of_participation', 'location', 'slug',]}),
        ('Кыргызский перевод', {'fields': ['name_exhibition_kg', 'period_kg', 'data_of_participation_kg', 'location_kg',]})
    ]


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'questions'
    ]

    fieldsets = [
        ('Русский основной', {'fields': ['name', 'email', 'phone', 'questions']}),
        ('Кыргызский перевод', {'fields': ['name_kg', 'email_kg', 'phone_kg', 'questions_kg']})
    ]

    def has_add_permission(self, request):
        return False


@admin.register(ManualVideo)
class ManualVideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    # fieldsets = [
    #     ('Русский основной', {'fields': ['name', 'description']}),
    #     ('Кыргызский перевод', {'fields': ['name_kg', 'description_kg']})
    # ]
