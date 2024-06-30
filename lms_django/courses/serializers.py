from rest_framework import serializers

from users.serializers import UserSerializer

from .models import (Category, Course, Lesson, Quiz, Chapter)


class AssignCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'clamped_title')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class CourseListSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview_description',
                  'created_by', 'categories')
        

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title',
                  'description', 'get_image')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'content', 'lesson_type', 'get_image',
                  'youtube_id')


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'lesson', 'question',
                  'answer', 'opt1', 'opt2', 'opt3', 'opt4')
        


class PublishedLessonMenuSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(status=Lesson.PUBLISHED).order_by('list_order')
        return super(PublishedLessonMenuSerializer, self).to_representation(data)


class LessonMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        list_serializer_class = PublishedLessonMenuSerializer
        fields = ('id', 'title')


class ChapterMenuSerializer(serializers.ModelSerializer):
    lessons = LessonMenuSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ('id', 'title', 'lessons')

