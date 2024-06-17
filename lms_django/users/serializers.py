from django.contrib.auth import get_user_model
from django.contrib.auth import  authenticate

from rest_framework import serializers

from study_groups.models import StudyGroup, School



class AccountSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','full_name')

class AccountConversationStudyGroupSerializer(serializers.ModelSerializer):
    school = AccountSchoolSerializer(many=False)
    class Meta:
        model = StudyGroup
        fields = ('id','grade', 'letter', 'school' )


class AccountUserSerializer(serializers.ModelSerializer):
    study_groups = AccountConversationStudyGroupSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'get_image', 'role', 'study_groups')


class UserSerializer(serializers.ModelSerializer):
    '''serializer for the user object'''
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class AuthSerializer(serializers.Serializer):
    '''serializer for the user authentication object'''
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        
        if not user:
            msg = ('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return user