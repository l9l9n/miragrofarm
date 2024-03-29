from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(verbose_name='Категории', max_length=150)
    slug = models.SlugField()
    objects = models.Manager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(verbose_name="Подкатегории", max_length=150)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return f"{self.name}"


class IconAnimal(models.Model):
    name = models.CharField(max_length=60, verbose_name='Тип животного')
    icon = models.ImageField(upload_to='icons/', verbose_name='Иконка')
    objects = models.Manager()

    class Meta:
        verbose_name = 'Иконка животного'
        verbose_name_plural = 'Иконки животного'

    def __str__(self):
        return f"{self.name}"


class FilePDF(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название PDF файла')
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'PDF файл'
        verbose_name_plural = 'PDF файлы'

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=150)
    slug_name = models.SlugField(verbose_name='Слаг')
    img_product = models.ImageField(upload_to='img_product/', verbose_name='Картинка лекарства')
    short_description = models.CharField(max_length=150, verbose_name='Короткое описание')
    icon_animal = models.ManyToManyField(IconAnimal, verbose_name='Иконка животного', related_name='products')
    description = models.TextField(verbose_name='Описание')
    compound = models.TextField(verbose_name='Состав')
    applying = models.TextField(verbose_name='Применение')
    waiting_time = models.TextField(verbose_name='Период ожидания')
    release_form = models.TextField(verbose_name='Форма выпуска')
    storage_date = models.TextField(verbose_name='Условия хранения')
    storage_conditions = models.TextField(verbose_name='Срок годности')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True,
                                     verbose_name='Какой подкатегории относится?')
    is_new_product = models.BooleanField(verbose_name='Является ли продукт новинкой', default=False)
    pdf_file = models.ManyToManyField(FilePDF, verbose_name='PDF файлы', related_name='products')
    objects = models.Manager()

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150, null=False)
    phone = models.IntegerField(verbose_name='Телефон', null=False)
    email = models.EmailField(verbose_name='email', null=True)
    date = models.DateTimeField('Дата создания заявки', auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-date']

    def __str__(self):
        return f"Имя {self.name}, Номер телефона {self.phone}, email {self.email}"


class Subscription(models.Model):
    email = models.EmailField(unique=True, verbose_name="Подписчики")
    objects = models.Manager()

    class Meta:
        verbose_name = 'Подписчик на рассылку'
        verbose_name_plural = 'Подписчики на рассылки'

    def __str__(self):
        return f"{self.email}"
