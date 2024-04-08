from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import News

from .serializers import (NewsListSerializer,)


@api_view(['GET'])
def get_news(request):
    news = News.objects.all()
    serializer = NewsListSerializer(news, many=True)
    return Response(serializer.data)
