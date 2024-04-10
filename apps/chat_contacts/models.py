from django.db import models


class ChatContacts(models.Model):
    chat_link = models.URLField(verbose_name="Ccылка для WhatSapp или Telegram")
    objects = models.Manager()

    class Meta:
        verbose_name = "Чат контакты"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.chat_link