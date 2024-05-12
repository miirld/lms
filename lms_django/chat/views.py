from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import (
    ConversationSerializer, ConversationMessageSerializer, ConversationDetailSerializer)
from .models import Conversation, ConversationMessage


@api_view(['GET'])
def conversation_list(request):
    conversations = Conversation.objects.filter(users__in=list([request.user]))
    serializer = ConversationSerializer(conversations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def conversation_detail(request, id):
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(id=id)
    serializer = ConversationDetailSerializer(conversation)

    return Response(serializer.data)


@api_view(['POST'])

def conversation_send_message(request, id):
     conversation = Conversation.objects.filter(users__in=list([request.user])).get(id=id)

     for user in conversation.users.all():
         if user != request.user:
             sent_to = user

     conversation_message = ConversationMessage.objects.create(
         conversation = conversation,
         body = request.data.get('body'),
         sent_to = sent_to,
         created_by = request.user
     )

     serializer = ConversationMessageSerializer(conversation_message)

     return Response(serializer.data)