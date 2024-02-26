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


@admin.register(QuestionsAndAnswers)
class QuestionsandanswersAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'questions'
    ]

