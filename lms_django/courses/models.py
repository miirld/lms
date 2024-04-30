from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Course(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликовано'),
    )

    created_by = models.ForeignKey(
        get_user_model(), related_name='courses', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Название')
    categories = models.ManyToManyField(
        Category, related_name='courses', verbose_name='Категории')
    preview_description = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Описание для превью')
    description = models.TextField(
        blank=True, null=True, verbose_name='Описание')
    created_at = models.DateField(
        auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(
        upload_to='uploads', blank=True, null=True, verbose_name='Изображение')
    status = models.CharField(
        max_length=25, choices=STATUS_CHOICES, default=DRAFT, verbose_name='Статус')

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return "https://placehold.co/600x400"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

