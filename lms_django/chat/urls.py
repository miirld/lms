from django.urls import path

from . import views



urlpatterns = [
    path('', views.conversation_list, name='conversation_list'),
    path('<int:id>/', views.conversation_detail, name='conversation_detail'),
    path('<int:id>/send/', views.conversation_send_message, name='conversation_send_message'),
]



