from django.db import models

from django.contrib.auth import get_user_model
from django.utils.timesince import timesince


class Conversation(models.Model):
    users = models.ManyToManyField(
        get_user_model(), related_name='conversations', verbose_name='Участники')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def modified_at_formatted(self):
        return timesince(self.created_at)
    
    
    class Meta:
        verbose_name = 'Беседа'
        verbose_name_plural = 'Беседы'
        


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(
        Conversation, related_name='messages', on_delete=models.CASCADE, verbose_name='Беседа')
    body = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    created_by = models.ForeignKey(
        get_user_model(), related_name='sent_messages', on_delete=models.CASCADE, verbose_name='От кого')
    sent_to = models.ForeignKey(
        get_user_model(), related_name='recieved_messages', on_delete=models.CASCADE, verbose_name='Кому')

    def created_at_formatted(self):
        return timesince(self.created_at)
    

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'