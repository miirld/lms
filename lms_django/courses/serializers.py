from rest_framework import serializers

from .models import Category, Course, Lesson, Quiz, Chapter

from django.contrib.auth import get_user_model





class AssignCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'clamped_title')


class CourseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'patronymic')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class CourseListSerializer(serializers.ModelSerializer):
    created_by = CourseUserSerializer(many=False)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'preview_description',
                  'created_by', 'categories')


class CourseMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'title',
                  'description')


class PublishedLessonMenuSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(status=Lesson.PUBLISHED)
        return super( PublishedLessonMenuSerializer, self).to_representation(data)

class LessonMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        list_serializer_class=PublishedLessonMenuSerializer
        fields = ('id', 'title')


class ChapterMenuSerializer(serializers.ModelSerializer):
    lessons = LessonMenuSerializer(many=True)
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'lessons')





class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'content', 'lesson_type',
                  'youtube_id')


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'lesson', 'question',
                  'answer', 'opt1', 'opt2', 'opt3')