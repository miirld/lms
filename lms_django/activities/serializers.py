from rest_framework import serializers

from .models import Activity

from courses.models import Lesson, Chapter, Course
from study_groups.models import StudyGroup, School





class LessonMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title')


class ChapterMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title')



class ActiveLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'status')


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('title', )

class ProgressLessonSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(many=False)
    class Meta:
        model = Lesson
        fields = ('title', 'chapter', )

class ProgressActivitySerializer(serializers.ModelSerializer):
    lesson = ProgressLessonSerializer(many=False)
    class Meta:
        model = Activity
        fields = ('id','status', 'lesson')

class ProgressCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','title' )






    