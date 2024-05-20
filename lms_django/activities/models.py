from django.db import models

from django.contrib.auth import get_user_model
from django.db import models

from courses.models import Course, Lesson


class Activity(models.Model):
    STARTED = 'started'
    DONE = 'done'

    STATUS_CHOICES = (
        (STARTED, 'В работе'),
        (DONE, 'Завершена'),
    )
    course = models.ForeignKey(
        Course, related_name='activities', on_delete=models.CASCADE, verbose_name='Курс')
    lesson = models.ForeignKey(
        Lesson, related_name='activities', on_delete=models.CASCADE , verbose_name='Урок')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STARTED, verbose_name='Статус')
    created_by = models.ForeignKey(
        get_user_model(), related_name='created_activities', on_delete=models.CASCADE, verbose_name='Создатель')
    participant = models.ForeignKey(get_user_model(), related_name='activities', on_delete=models.CASCADE, verbose_name='Участник')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')


    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'

