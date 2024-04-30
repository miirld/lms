from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .models import Course, Category

from .serializers import (CourseSerializer, CategorySerializer)


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
    courses = Course.objects.all().order_by('created_at')
    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])
    paginator = CoursesPageNumberPagination()
    paginator.page_size = 5
    results = paginator.paginate_queryset(courses, request)
    serializer = CourseSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all().order_by('title')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
