from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_activity_courses, name='get_activity_courses'),
    path('lesson/<int:lesson_id>/', views.get_lesson_status, name='get_active_lesson'),
    path('get-for-assign/', views.get_data_for_activity, name='get_data_for_activity'),
    path('assign/', views.assign_activity, name='assign_activity'),
    path('mark-as-done/<int:lesson_id>/', views.mark_as_done),
]