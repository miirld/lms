from django.contrib import admin

from .models import Conversation, ConversationMessage


class ConversationMessageAdmin(admin.ModelAdmin):
    list_filter = ['sent_to']

admin.site.register(Conversation)
admin.site.register(ConversationMessage, ConversationMessageAdmin)


# Register your models here.
