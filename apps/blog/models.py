from django.db import models


class Events(models.Model):
    title = models.CharField(verbose_name='Событие', max_length=150)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Дата создан', auto_now_add=True)
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


class ExhibitionCalendar(models.Model):
    name_exhibition = models.TextField(max_length=150, verbose_name='Календарь выставок')
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
    img_preview = models.ImageField(upload_to='img_preview_video/')
    link = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    objects = models.Manager()

    class Meta:
        verbose_name = 'Видео инструкция'
        verbose_name_plural = 'Видео инструкции'


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
    pass


class OurPartners(models.Model):
    pass


class Contacts(models.Model):
    pass
