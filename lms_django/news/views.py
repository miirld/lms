from datetime import datetime

from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .models import News
from .serializers import (NewsListSerializer,)






@api_view(['GET'])
def get_news(request):
    types = request.GET.getlist('types[]', [])
    dates = request.GET.getlist('dates[]', [])
    news = News.objects.filter(status=News.PUBLISHED)
    news = news.filter(created_for_study_groups__in=request.user.study_groups.all()) | news.filter(created_for_study_groups = None)
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
        news = news.filter(created_at__range=(dates[0], dates[1]))
    news = news.order_by('-created_at')

    paginator = PageNumberPagination()
    paginator.page_size = 3
    results = paginator.paginate_queryset(news, request)
    serializer = NewsListSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)
