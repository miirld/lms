from django.urls import path

from . import views



urlpatterns = [
    path('', views.existing_conversation_interlocutors, name='existing_conversation_interlocutors'),
    path('search/', views.search_interlocutors, name='search_interlocutors'),
    path('<int:user_id>/', views.conversation_detail_get_or_create, name='conversation_detail'),
    path('<int:conversation_id>/send/', views.conversation_send_message, name='conversation_send_message'),
]




