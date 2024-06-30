from rest_framework import serializers
from .models import StudyGroup, School



class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','short_name', 'full_name')

class StudyGroupSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(many=False)
    class Meta:
        model = StudyGroup
        fields= ('id', 'grade', 'letter', 'school')

        