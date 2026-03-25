from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


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
    




class Category(models.TextChoices):
    SEO = 'seo', 'SEO'
    PPC = 'ppc', 'PPC'
    SMM = 'smm', 'SMM'
    DEV = 'development', 'Разработка'


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=20, choices=Category.choices)
    excerpt = models.TextField('Короткий опис', max_length=300, blank=True)
    content = CKEditor5Field('Контент', config_name='extends')
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    reading_time = models.PositiveIntegerField('Час читання (хв)', default=5)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})