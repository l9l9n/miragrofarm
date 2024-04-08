from django.db import models


class ChatContacts(models.Model):
    chat_link = models.URLField(verbose_name="Ccылка для WhatSapp или Telegram")

    class Meta:
        verbose_name = "Чат контакты"
        verbose_name_plural = verbose_name
