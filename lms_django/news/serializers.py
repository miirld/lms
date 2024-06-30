from rest_framework import serializers

from users.serializers import UserSerializer

from .models import News


class NewsListSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False)
    class Meta:
        model = News
        fields = ('id', 'content', 'created_at', 'get_image', 'created_by')
