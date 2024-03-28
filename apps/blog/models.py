from django.db import models


class Events(models.Model):
    title = models.CharField(verbose_name='Событие', max_length=150)
    short_description = models.TextField(verbose_name='Короткое описание', max_length=250)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateField(verbose_name='Дата события', auto_now_add=True)
    image = models.ImageField(verbose_name='Картинка', upload_to='img_blog/')
    is_publish = models.BooleanField(verbose_name="Опубликовано")
    objects = models.Manager()

    class Meta:
        verbose_name = 'Событиe'
        verbose_name_plural = 'События'

    def __str__(self):
        return f"{self.title}"


class Public(models.Model):
    title = models.CharField(verbose_name='Публикации', max_length=150)
    short_description = models.TextField(verbose_name='Короткое описание', max_length=250)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateField(verbose_name='Добавлено', auto_now_add=True)
    image = models.ImageField(verbose_name='Картинка', upload_to='img_public/')
    is_publish = models.BooleanField(verbose_name="Опубликовано")
    objects = models.Manager()

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f"{self.title}"


class ExhibitionCalendar(models.Model):
    name_exhibition = models.TextField(max_length=320, verbose_name='Название выставки')
    period = models.CharField(verbose_name='Период', max_length=30)
    data_of_participation = models.CharField(verbose_name='Дата участия', max_length=100)
    location = models.CharField(verbose_name='Место проведения выставки', max_length=100)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Календарь выставки'
        verbose_name_plural = 'Календарь выставок'

    def __str__(self):
        return f"{self.name_exhibition}"


class ManualVideo(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название видео')
    description = models.TextField(verbose_name='Описание видео')
    img_preview = models.ImageField(verbose_name="Превью видео", upload_to='img_preview_video/')
    link = models.CharField(verbose_name='Ссылка на видео', max_length=300)
    created = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    objects = models.Manager()

    class Meta:
        verbose_name = 'Видео инструкция'
        verbose_name_plural = 'Видео инструкции'

    def __str__(self):
        return self.name


class Questions(models.Model):
    name = models.CharField(max_length=90, verbose_name='Имя', null=True)
    email = models.EmailField(verbose_name='Почта', null=True)
    phone = models.CharField(max_length=13, verbose_name='Телефон')
    questions = models.TextField(verbose_name='Вопросы и ответы', null=True)
    date = models.DateTimeField('Дата вопроса', auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'
        ordering = ['-date']

    def __str__(self):
        return f"Имя {self.name}, Номер телефона {self.phone}, email {self.email}"


class Service(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя', null=True)
    description = models.TextField(max_length=400, verbose_name='Описание')
    image = models.ImageField(verbose_name='Картинка', upload_to="img_service/")
    objects = models.Manager()

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f"{self.name}"


class OurPartners(models.Model):
    img_partner = models.ImageField(verbose_name="Партнеры (лого)", upload_to="img_partner/")
    objects = models.Manager()

    class Meta:
        verbose_name = 'Логотип партнера'
        verbose_name_plural = 'Логотип партнеров'


class Contacts(models.Model):
    owner = models.CharField(verbose_name="Владелец", max_length=180)
    company = models.CharField(verbose_name="Наименование компании или ОСО", max_length=180)
    phone = models.CharField(verbose_name='Телефон', max_length=13)
    email = models.EmailField(verbose_name="Почта", max_length=90)
    address = models.CharField(verbose_name="Адрес", max_length=100)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.owner
