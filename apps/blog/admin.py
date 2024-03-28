from django.contrib import admin
from .models import *


@admin.register(Events)
class BlogEventsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'short_description',
        'description',
        'created_at',
        'image',
        'is_publish',
    ]

    fieldsets = [
        ('Русский основной', {'fields': ['title', 'short_description', 'description', 'image', 'is_publish',]}),
        ('Кыргызский перевод', {'fields': ['title_kg', 'short_description_kg', 'description_kg']})
    ]


@admin.register(Public)
class BlogPublicAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'short_description',
        'description',
        'created_at',
        'image',
        'is_publish',
    ]

    fieldsets = [
        ('Русский основной', {'fields': ['title', 'short_description', 'description', 'image', 'is_publish',]}),
        ('Кыргызский перевод', {'fields': ['title_kg', 'short_description_kg', 'description_kg',]})
    ]


@admin.register(ExhibitionCalendar)
class ExhibitionCalendarAdmin(admin.ModelAdmin):
    list_display = [
        'name_exhibition',
        'period',
        'data_of_participation',
        'location',
    ]

    fieldsets = [
        ('Русский основной', {'fields': ['name_exhibition', 'period', 'data_of_participation', 'location',]}),
        ('Кыргызский перевод', {'fields': ['name_exhibition_kg', 'location_kg',]})
    ]


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'questions',
    ]

    fieldsets = [
        ('Русский основной', {'fields': ['name', 'email', 'phone', 'questions']}),
        ('Кыргызский перевод', {'fields': ['name_kg', 'email_kg', 'phone_kg', 'questions_kg']})
    ]

    def has_add_permission(self, request):
        return False


@admin.register(Service)
class BlogServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'image',
    ]

    fieldsets = [
        ('Русский основной', {'fields': ['name', 'description', 'image',]}),
        ('Кыргызский перевод', {'fields': ['name_kg', 'description_kg']})
    ]


@admin.register(ManualVideo)
class ManualVideoAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'img_preview',
        'link',
    ]

    fieldsets = [
        ('Русский основной', {'fields': ['name', 'description', 'img_preview', 'link']}),
        ('Кыргызский перевод', {'fields': ['name_kg', 'description_kg']})
    ]


@admin.register(OurPartners)
class OurPartnersAdmin(admin.ModelAdmin):
    list_display = ['img_partner',]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'company',
        'phone',
        'email',
        'address',
    ]
