from rest_framework import serializers
from .models import StudyGroup, School

from courses.serializers import AssignCourseSerializer


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','short_name')

class StudyGroupSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(many=False)
    courses = AssignCourseSerializer(many=True)
    class Meta:
        model = StudyGroup
        fields= ('id', 'grade', 'letter', 'school', 'courses' )