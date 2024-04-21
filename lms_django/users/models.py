from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from study_groups.models import StudyGroup


class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=150, blank=True, verbose_name='Отчество')
    avatar = models.ImageField(upload_to='users', blank=True, null=True, verbose_name='Аватар')
    studygroups = models.ManyToManyField(StudyGroup, related_name='members', verbose_name='Класс', blank=True)
    

    def __str__(self):
        return self.username
    
    def get_image(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return 'https://placehold.co/48x48'
