from rest_framework import serializers

from .models import Activity

from courses.models import Lesson, Chapter, Course
from study_groups.models import StudyGroup, School

from django.contrib.auth import get_user_model


class ActiveLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'status')


class ProgressSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'short_name')


class OnlyStudents(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(role=get_user_model().STUDENT)
        return super(OnlyStudents, self).to_representation(data)

class ProgressUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        list_serializer_class=OnlyStudents
        fields = ('id', 'first_name', 'last_name', 'patronymic')
        

# class ProgressStudyGroupSerializer(serializers.ModelSerializer):
#     school = ProgressSchoolSerializer(many=False)
#     members = ProgressUserSerializer(many=True)
#     class Meta:
#         model = StudyGroup
#         fields = ('id', 'grade', 'letter', 'school', 'members')


class ProgressStudyGroupSerializer(serializers.ModelSerializer):
    school = ProgressSchoolSerializer(many=False)
    class Meta:
        model = StudyGroup
        fields = ('id', 'grade', 'letter', 'school')

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






    