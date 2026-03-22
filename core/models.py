from django.db import models
from django.urls import reverse


class Case(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    category = models.CharField(max_length=100, blank=True, verbose_name='Категория')
    niche = models.CharField(max_length=100, blank=True, verbose_name='Ниша')
    country = models.CharField(max_length=100, blank=True, verbose_name='Страна')

    short_description = models.TextField(blank=True, verbose_name='Короткое описание')
    hero_subtitle = models.TextField(blank=True, verbose_name='Подзаголовок на странице кейса')

    image = models.ImageField(upload_to='cases/', verbose_name='Главное изображение')
    detail_image = models.ImageField(upload_to='cases/details/', blank=True, null=True, verbose_name='Изображение внутри кейса')

    stat_1_value = models.CharField(max_length=50, blank=True, verbose_name='Стат 1 значение')
    stat_1_label = models.CharField(max_length=150, blank=True, verbose_name='Стат 1 подпись')
    stat_2_value = models.CharField(max_length=50, blank=True, verbose_name='Стат 2 значение')
    stat_2_label = models.CharField(max_length=150, blank=True, verbose_name='Стат 2 подпись')
    stat_3_value = models.CharField(max_length=50, blank=True, verbose_name='Стат 3 значение')
    stat_3_label = models.CharField(max_length=150, blank=True, verbose_name='Стат 3 подпись')
    stat_4_value = models.CharField(max_length=50, blank=True, verbose_name='Стат 4 значение')
    stat_4_label = models.CharField(max_length=150, blank=True, verbose_name='Стат 4 подпись')

    task = models.TextField(blank=True, verbose_name='Задача проекта')
    what_we_did = models.TextField(blank=True, verbose_name='Что сделали')
    result = models.TextField(blank=True, verbose_name='Результат')
    quote = models.TextField(blank=True, verbose_name='Цитата')

    service = models.CharField(max_length=100, blank=True, verbose_name='Услуга')
    period = models.CharField(max_length=100, blank=True, verbose_name='Период')

    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    from django.db import models
from django.urls import reverse


class Case(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    category = models.CharField(max_length=100, blank=True, verbose_name='Категория')
    niche = models.CharField(max_length=100, blank=True, verbose_name='Ниша')
    country = models.CharField(max_length=100, blank=True, verbose_name='Страна')

    short_description = models.TextField(blank=True, verbose_name='Короткое описание')
    hero_subtitle = models.TextField(blank=True, verbose_name='Подзаголовок на странице кейса')

    image = models.ImageField(upload_to='cases/', verbose_name='Главное изображение')
    detail_image = models.ImageField(upload_to='cases/details/', blank=True, null=True, verbose_name='Изображение внутри кейса')

    stat_1_value = models.CharField(max_length=50, blank=True, verbose_name='Стат 1 значение')
    stat_1_label = models.CharField(max_length=150, blank=True, verbose_name='Стат 1 подпись')
    stat_2_value = models.CharField(max_length=50, blank=True, verbose_name='Стат 2 значение')
    stat_2_label = models.CharField(max_length=150, blank=True, verbose_name='Стат 2 подпись')
    stat_3_value = models.CharField(max_length=50, blank=True, verbose_name='Стат 3 значение')
    stat_3_label = models.CharField(max_length=150, blank=True, verbose_name='Стат 3 подпись')
    stat_4_value = models.CharField(max_length=50, blank=True, verbose_name='Стат 4 значение')
    stat_4_label = models.CharField(max_length=150, blank=True, verbose_name='Стат 4 подпись')

    task = models.TextField(blank=True, verbose_name='Задача проекта')
    what_we_did = models.TextField(blank=True, verbose_name='Что сделали')
    result = models.TextField(blank=True, verbose_name='Результат')
    quote = models.TextField(blank=True, verbose_name='Цитата')

    service = models.CharField(max_length=100, blank=True, verbose_name='Услуга')
    period = models.CharField(max_length=100, blank=True, verbose_name='Период')

    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('case_detail', kwargs={'slug': self.slug})

    def tags(self):
        return [tag for tag in [self.category, self.niche, self.country] if tag]