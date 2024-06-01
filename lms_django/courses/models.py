from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from study_groups.models import StudyGroup


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
        get_user_model(), related_name='my_courses', on_delete=models.CASCADE, verbose_name='Автор')
    created_for = models.ManyToManyField(
        StudyGroup, related_name='courses', verbose_name='Классы')
    title = models.CharField(max_length=255, verbose_name='Название')
    categories = models.ManyToManyField(
        Category, related_name='courses', verbose_name='Категории')
    preview_description = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Описание для превью')
    description = models.TextField(
        blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(
        upload_to='uploads', blank=True, null=True, verbose_name='Изображение')
    status = models.CharField(
        max_length=25, choices=STATUS_CHOICES, default=DRAFT, verbose_name='Статус')

    @property
    def clamped_title(self):
        if len(self.title) > 50:
            return self.title[0:50] + '...'
        else:
            return self.title

    clamped_title.fget.short_description = 'Текст'

    def __str__(self):
        return self.clamped_title

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return "https://placehold.co/600x400"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'



class Chapter(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    course = models.ForeignKey(
        Course, related_name='chapters', on_delete=models.CASCADE, verbose_name='Курс')
    list_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('course', 'list_order')
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'


class Lesson(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликован'),
    )

    ARTICLE = 'article'
    QUIZ = 'quiz'
    VIDEO = 'video'

    CHOICES_LESSON_TYPE = (
        (ARTICLE, 'Статья'),
        (QUIZ, 'Викторина'),
        (VIDEO, 'Видео'),

    )

    course = models.ForeignKey(
        Course, related_name='lessons', on_delete=models.CASCADE, verbose_name='Курс')
    chapter = models.ForeignKey (Chapter, related_name='lessons', on_delete=models.CASCADE, verbose_name='Глава')
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True, null=True, verbose_name='Контент')
    status = models.CharField(
        max_length=20, choices=CHOICES_STATUS, default=DRAFT, verbose_name='Статус')
    lesson_type = models.CharField(
        max_length=20, choices=CHOICES_LESSON_TYPE, default=ARTICLE, verbose_name='Тип')
    youtube_id = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Ссылка на видео')
    list_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('chapter', 'list_order')
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Quiz(models.Model):
    lesson = models.ForeignKey(
        Lesson, related_name='quizzes', on_delete=models.CASCADE, verbose_name='Урок')
    question = models.CharField(
        max_length=255, null=True, verbose_name='Вопрос')
    answer = models.CharField(
        max_length=255, null=True, verbose_name='Правильный ответ')
    opt1 = models.CharField(max_length=255, null=True,
                            verbose_name='Ответ 1')
    opt2 = models.CharField(max_length=255, null=True,
                            verbose_name='Ответ 2')
    opt3 = models.CharField(max_length=255, null=True,
                            verbose_name='Ответ 3')

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'
