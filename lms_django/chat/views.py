from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import (
    ConversationSerializer, ConversationMessageSerializer, ConversationDetailSerializer, ConversationUserSerializer)
from .models import Conversation, ConversationMessage

from django.contrib.auth import get_user_model

from django.db.models.functions import Concat
from django.db.models import CharField


@api_view(['GET'])
def existing_conversation_interlocutors(request):
    conversations = Conversation.objects.filter(
        users__in=list([request.user]))
    users = get_user_model().objects.filter(
        conversations__in=conversations).distinct().exclude(id=request.user.id)
    serializer = ConversationUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def conversation_detail_get_or_create(request, user_id):
    user = get_user_model().objects.get(id=user_id)

    conversations = Conversation.objects.filter(
        users__in=list([request.user])).filter(users__in=list([user]))

    if conversations.exists():
        conversation = conversations.first()
    else:
        conversation = Conversation.objects.create()
        conversation.users.add(user, request.user)
        conversation.save()

    serializer = ConversationDetailSerializer(conversation)

    return Response(serializer.data)


@api_view(['GET'])
def search_interlocutors(request):
    search = request.GET.get('search', '')
    users = get_user_model().objects.annotate(full_name=Concat(
        'first_name', 'last_name', 'patronymic', output_field=CharField())).filter(full_name__icontains=search).exclude(id=request.user.id)
    serializer = ConversationUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def conversation_send_message(request):
    conversation_id = request.data.get('conversation_id')
    conversation = Conversation.objects.filter(
        users__in=list([request.user])).get(id=conversation_id)


    conversation_message = ConversationMessage.objects.create(
        conversation=conversation,
        body=request.data.get('body'),
        created_by=request.user
    )

    serializer = ConversationMessageSerializer(conversation_message)

    return Response(serializer.data)
