from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Conversation, ConversationMessage
from study_groups.models import StudyGroup
from study_groups.serializers import SchoolSerializer


class ConversationStudyGroupSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(many=False)
    class Meta:
        model = StudyGroup
        fields = ('id','grade', 'letter', 'school' )


class ConversationUserSerializer(serializers.ModelSerializer):
    study_groups = ConversationStudyGroupSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'get_image', 'role', 'study_groups')



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
