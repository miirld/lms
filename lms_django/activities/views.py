from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from study_groups.serializers import (StudyGroupSerializer)
from study_groups.models import (StudyGroup)
from courses.models import (Lesson, Course)

from .models import (Activity)

from django.contrib.auth import get_user_model

from rest_framework import status

from courses.views import CoursesPageNumberPagination
from courses.serializers import CourseListSerializer

from .serializers import ActiveLessonSerializer


@api_view(['GET'])
def get_activity_courses(request):
    category_id = request.GET.get('category_id', '')
    courses = Course.objects.none()
    for activity in request.user.activities.all():
        if activity.course not in courses:
            courses |= Course.objects.filter(id=activity.course.id)
    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])
    courses = courses.order_by('-created_at')
    paginator = CoursesPageNumberPagination()
    paginator.page_size = 4
    results = paginator.paginate_queryset(courses, request)
    serializer = CourseListSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_data_for_activity(request):
    if request.user.role == get_user_model().TEACHER:
        study_groups = StudyGroup.objects.filter(
            members__in=([request.user.id]))
        study_groups_serializer = StudyGroupSerializer(study_groups, many=True)
        return Response(study_groups_serializer.data)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def assign_activity(request):
    if request.user.role == get_user_model().TEACHER:
        study_group_id = request.data.get('study_group')
        course_id = request.data.get('course')
        users = get_user_model().objects.filter(study_groups__in=(
            [study_group_id])).filter(role=get_user_model().STUDENT)
        course = Course.objects.get(id=course_id)
        lessons = Lesson.objects.filter(course=course_id)

        for lesson in lessons:
            for user in users:
                Activity.objects.get_or_create(
                    course=course,
                    lesson=lesson,
                    status=Activity.STARTED,
                    created_by=request.user,
                    participant=user
                )
        return Response()
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    


@api_view(['GET'])
def get_lesson_status(request, lesson_id):
    activity = Activity.objects.get(lesson__id=lesson_id, participant = request.user)
    serializer = ActiveLessonSerializer(activity)
    return Response(serializer.data)

@api_view(['POST'])
def mark_as_done(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)

    activity = Activity.objects.get(
        participant=request.user, lesson=lesson)
    
    activity.status = Activity.DONE
    activity.save()

    serializer = ActiveLessonSerializer(activity)


    return Response(serializer.data)