from rest_framework import serializers

from .models import News

from django.contrib.auth import get_user_model


class MediaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'patronymic','get_image')


class NewsListSerializer(serializers.ModelSerializer):
    created_by = MediaUserSerializer(many=False)
    class Meta:
        model = News
        fields = ('id', 'content', 'created_at', 'get_image', 'created_by')
