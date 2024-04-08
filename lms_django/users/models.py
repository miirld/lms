from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=150, blank=True, verbose_name='Отчество')
    

    def __str__(self):
        return self.username
