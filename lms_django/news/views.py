from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .models import News

from .serializers import (NewsListSerializer,)


@api_view(['GET'])
def get_news(request):
    news = News.objects.all().order_by('-created_at')
    paginator = PageNumberPagination()
    paginator.page_size = 3
    results = paginator.paginate_queryset(news, request)
    serializer = NewsListSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)
