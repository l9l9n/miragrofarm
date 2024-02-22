from django.db import models
from django.utils import timezone

from .. products.models import Product


class Events(models.Model):
    title = models.CharField(verbose_name='События', max_length=150)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    image = models.CharField(verbose_name='Картинка', max_length=150)
    slug = models.SlugField()
    objects = models.Manager()

    class Meta:
        verbose_name = 'Событиe'
        verbose_name_plural = 'События'

    def __str__(self):
        return f"{self.title}"


class Public(models.Model):
    title = models.CharField(verbose_name='Публикации', max_length=150)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    image = models.CharField(verbose_name='Картинка', max_length=200)
    slug = models.SlugField()
    objects = models.Manager()

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f"{self.title}"


class NewProducts(models.Model):
    product_name = models.CharField(verbose_name='Имя продукта', max_length=150)
    slug = models.SlugField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='Новинка')
    objects = models.Manager()

    class Meta:
        verbose_name = 'Новинка'
        verbose_name_plural = 'Новинки'

    def __str__(self):
        return f"{self.product_name}"


class ExhibitionCalendar(models.Model):
    name_exhibition = models.TextField(verbose_name='Календарь выставок')
    period = models.CharField(verbose_name='Период', max_length=100)
    data_of_participation = models.CharField(verbose_name='Дата участия', max_length=100)
    location = models.CharField(verbose_name='Место проведения выставки', max_length=100)
    slug = models.SlugField()
    objects = models.Manager()

    class Meta:
        verbose_name = 'Календарь выставки'
        verbose_name_plural = 'Календарь выставок'

    def __str__(self):
        return f"{self.name_exhibition}"


class ManualVideo(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название видео')
    description = models.TextField(verbose_name='Описание видео')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')


class QuestionsAndAnswers(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя', null=True)
    email = models.EmailField(verbose_name='Почта', null=True)
    telephone = models.CharField(max_length=120, verbose_name='Телефон')
    question = models.TextField(verbose_name='Вопросы и ответы', null=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'
        question = ['-date']

    def __str__(self):
        return f"Имя {self.name}, Номер телефона {self.phone}, email {self.email}"


