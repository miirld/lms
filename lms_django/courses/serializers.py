from rest_framework import serializers

from .models import Category, Course

from django.contrib.auth import get_user_model


class CourseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'patronymic')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class CourseSerializer(serializers.ModelSerializer):
    created_by = CourseUserSerializer(many=False)
    categories = CategorySerializer(many=True)
    class Meta:
        model = Course
        fields = ('id', 'title', 'preview_description', 'created_by', 'categories')
