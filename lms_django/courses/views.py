from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .models import Course, Category, Lesson, Quiz


from .serializers import (CategorySerializer, CourseListSerializer,
                          QuizSerializer, CourseMenuSerializer, ChapterMenuSerializer, LessonSerializer, AssignCourseSerializer)

from study_groups.serializers import (StudyGroupSerializer)


class CoursesPageNumberPagination(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })




@api_view(['GET'])
def get_courses(request):
    category_id = request.GET.get('category_id', '')
    courses = Course.objects.filter(status=Course.PUBLISHED)
    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])
    courses = courses.order_by('-created_at')
    paginator = CoursesPageNumberPagination()
    paginator.page_size = 2
    results = paginator.paginate_queryset(courses, request)
    serializer = CourseListSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all().order_by('title')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, id):
    course = Course.objects.get(id=id)
    course_serializer = CourseMenuSerializer(course)
    chapter_serializer = ChapterMenuSerializer(course.chapters.all().order_by('list_order'), many=True)

    return Response({
        'course': course_serializer.data,
        'chapters': chapter_serializer.data
    })


@api_view(['GET'])
def get_quiz(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    serializer = QuizSerializer(lesson.quiz)
    return Response(serializer.data)


@api_view(['GET'])
def get_lesson(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    serializer = LessonSerializer(lesson)
    return Response(serializer.data)
