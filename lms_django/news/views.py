from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .models import News

from .serializers import (NewsListSerializer,)


from datetime import datetime

from django.utils import timezone


@api_view(['GET'])
def get_news(request):
    types = request.GET.getlist('types[]', [])
    dates = request.GET.getlist('dates[]', [])

    news = News.objects.filter(status=News.PUBLISHED)
    news = news.filter(created_for_groups__in=request.user.groups.all()) | news.filter(created_for_groups = None)
    news = news.filter(created_for_studygroups__in=request.user.studygroups.all()) | news.filter(created_for_studygroups = None)
    news = news.distinct()
    

    if types:
        news = news.filter(type__in=types)
    if dates:
        dates = [datetime.date((datetime.fromtimestamp(int(date)/1000)))
                 for date in dates]
        dates[0] = timezone.make_aware(datetime.combine(
            dates[0], datetime.min.time()), timezone=timezone.get_current_timezone())
        dates[1] = timezone.make_aware(datetime.combine(
            dates[1], datetime.max.time()), timezone=timezone.get_current_timezone())
        news = News.objects.filter(created_at__range=(dates[0], dates[1])) | News.objects.filter(
            created_at__date=dates[0]) & News.objects.filter(created_at__date=dates[1])
    news = news.order_by('-created_at')

    paginator = PageNumberPagination()
    paginator.page_size = 3
    results = paginator.paginate_queryset(news, request)
    serializer = NewsListSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)
