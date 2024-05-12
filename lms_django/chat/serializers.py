from rest_framework import serializers

from .models import Conversation, ConversationMessage

from django.contrib.auth import get_user_model





class ConversationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'get_image')



class ConversationSerializer(serializers.ModelSerializer):
    users = ConversationUserSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ('id', 'users', 'modified_at_formatted')


class ConversationMessageSerializer(serializers.ModelSerializer):
    sent_to = ConversationUserSerializer(read_only=True)
    created_by = ConversationUserSerializer(read_only=True)

    class Meta:
        model = ConversationMessage
        fields = ('id', 'sent_to', 'created_by',
                  'created_at_formatted', 'body')


class ConversationDetailSerializer(serializers.ModelSerializer):
    messages = ConversationMessageSerializer(read_only=True, many=True)

    class Meta:
        model = Conversation
        fields = ('id', 'users', 'modified_at_formatted', 'messages')
