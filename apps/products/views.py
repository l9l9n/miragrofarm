import requests
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from .filters import ProductFilter
from .models import Product, Order, Subscription
from rest_framework import generics, status
from .serializers import ProductDetailSerializer, OrderSerializer, ProductListSerializer, SubscriptionSerializer
from rest_framework.permissions import AllowAny

from config.settings.base_set import TELEGRAM_BOT_TOKEN, EMAIL_HOST_USER


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = ProductFilter
    ordering_fields = ('name',)
    search_fields = ['name', 'slug_name']

    def get_queryset(self):
        queryset = Product.objects.all()
        icon_id = self.kwargs.get('icon_id')
        if icon_id is not None:
            queryset = queryset.filter(icon_animal__id=icon_id)
        return queryset


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Product.objects.all()
        icon_id = self.kwargs.get('icon_id')
        if icon_id is not None:
            queryset = queryset.filter(icon_animal__id=icon_id)
        return queryset


class OrderViewSet(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            # Формируем текст сообщения
            message_text = f"Получен новый заказ:\n"
            message_text += f"Номер заказа: {order.id}\n"
            message_text += f"Тел: {order.phone}\n"
            message_text += f"Имя: {order.name}\n"
            message_text += f"Email: {order.email}\n"
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


class SubscribeAPIView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            # Отправляем email уведомление
            subject = 'Подписка на рассылку'
            message = 'Вы успешно подписались на рассылку miragrofarm.'
            email_from = EMAIL_HOST_USER
            recipient_list = [email]
            try:
                # Отправляем email
                send_mail(subject, message, email_from, recipient_list)

                # Отправляем уведомление об успешной подписке в Telegram
                chat_id = "-1001982487239"  # Замените на ваш реальный chat_id
                bot_token = TELEGRAM_BOT_TOKEN  # Замените на ваш реальный токен
                url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
                message_text = f"Новая подписка на рассылку: {email}"
                payload = {"chat_id": chat_id, "text": message_text}
                response = requests.post(url, json=payload)

                return Response({"message": "Email sent and subscription notification sent to Telegram"},
                                status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": f"Error sending email or notification: {e}"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)


class NewProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Product.objects.filter(is_new_product=True)
        icon_id = self.kwargs.get('icon_id')
        if icon_id is not None:
            queryset = queryset.filter(icon_animal__id=icon_id)
        return queryset
