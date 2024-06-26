from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.conf import settings
from study_groups.models import StudyGroup


class News (models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликовано'),
    )

    ARTICLE = 'article'
    MESSAGE = 'message'

    TYPE_CHOICES = (
        (ARTICLE, 'Статья'),
        (MESSAGE, 'Объявление')
    )

    created_by = models.ForeignKey(
        get_user_model(), related_name='news', on_delete=models.CASCADE, verbose_name='Автор')
    created_for_study_groups = models.ManyToManyField(
        StudyGroup, related_name='news', verbose_name='Класс читателей', blank=True)
    content = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    status = models.CharField(
        max_length=25, choices=STATUS_CHOICES, default=DRAFT, verbose_name='Статус')
    type = models.CharField(
        max_length=25, choices=TYPE_CHOICES, default=ARTICLE, verbose_name='Тип')
    image = models.ImageField(
        upload_to='news', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.clamped_content

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return None

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



    @property
    def clamped_content(self):
        if len(self.content)>100:
            return self.content[0:100] + '...'
        else:
            return self.content

    
    clamped_content.fget.short_description = 'Текст'
    


