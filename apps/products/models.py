from django.db import models


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
    name = models.CharField(verbose_name="Подкатегории", max_length=130)
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


class Product(models.Model):
    APPLY_CHOICES = (
        ('fish', 'рыбы'),
        ('bird', 'птицы'),
        ('cattle', 'крупный рогатый скот'),
        ('small cattle', 'мелкий рогатый скот'),
        ('pig', 'свиньи'),
        ('horse', 'лошади'),
    )
    name = models.CharField(verbose_name='Название продукта', max_length=255)
    short_description = models.CharField(max_length=95, verbose_name='Короткое описание')
    icon_animal = models.ManyToManyField(IconAnimal, verbose_name='Иконка животного', related_name='products')
    description = models.TextField(verbose_name='Описание')
    compound = models.TextField(verbose_name='Состав')
    applying = models.CharField(verbose_name='Применение', choices=APPLY_CHOICES, max_length=50)
    waiting_time = models.TextField(verbose_name='Период ожидания')
    release_form = models.TextField(verbose_name='Форма выпуска')
    storage_date = models.TextField(verbose_name='Состав')
    storage_conditions = models.TextField(verbose_name='Срок хранения')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True,
                                     verbose_name='Какой подкатегории относится?')
    is_new_product = models.BooleanField(verbose_name='Является ли продукт новинкой')
    objects = models.Manager()

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255, null=False)
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
