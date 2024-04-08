from django.contrib import admin
from .models import ChatContacts


@admin.register(ChatContacts)
class ChatContactAdmin(admin.ModelAdmin):
    list_display = [
        "chat_link",
    ]

