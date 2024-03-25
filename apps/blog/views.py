import requests
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from config.settings.base_set import TELEGRAM_BOT_TOKEN
from .models import Events, Public, Questions, Service
from .serializers import EventSerializer, PublicSerializer, QuestionsSerializer, ServiceSerializer


class BlogEventsListAPIView(generics.ListAPIView):

    queryset = Events.objects.all()
    serializer_class = EventSerializer


class PublicBlogListAPIView(generics.ListAPIView):

    queryset = Public.objects.all()
    serializer_class = PublicSerializer


class QuestionsListAPIView(generics.CreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

    def post(self, request, *args, **kwargs):
        serializer = QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            # Формируем текст сообщения
            message_text = f"Поступил новый вопрос:\n"
            message_text += f"ID вопроса: {order.id}\n"
            message_text += f"Тел: {order.phone}\n"
            message_text += f"Имя: {order.name}\n"
            message_text += f"Email: {order.email}\n"
            message_text += f"Вопрос: {order.questions}\n"
            # Отправляем сообщение в Telegram
            chat_id = "-1001982487239"  # Замените на ваш реальный chat_id
            bot_token = TELEGRAM_BOT_TOKEN  # Замените на ваш реальный токен
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {"chat_id": chat_id, "text": message_text}
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "Failed to send message to Telegram"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception as e:
                return Response({"error": f"Error sending message to Telegram: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceListAPIView(generics.CreateAPIView):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer