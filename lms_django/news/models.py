from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class News (models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликовано'),
    )

    created_by = models.ForeignKey(
        get_user_model(), related_name='news', on_delete=models.CASCADE, verbose_name='Автор')
    created_for = models.ManyToManyField(
        get_user_model(), related_name='allowed_news', verbose_name='Новость для')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    short_description = models.TextField(verbose_name='Короткое описание')
    long_description = models.TextField(verbose_name='Длинное описание')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время создания')
    status = models.CharField(
        max_length=25, choices=STATUS_CHOICES, default=DRAFT, verbose_name='Статус')
    image = models.ImageField(
        upload_to='news', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return "https://placehold.co/4000x2000"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
