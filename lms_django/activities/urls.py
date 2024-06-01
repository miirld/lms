from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_activity_courses, name='get_activity_courses'),
    path('progress/', views.get_progress_courses, name='get_progress_courses'),
    path('course-progress/<int:course_id>/', views.get_course_name, name='get_course_name'),
    path('course-progress/<int:course_id>/groups', views.get_progress, name='get_progress'),
    path('lesson/<int:lesson_id>/', views.get_lesson_status, name='get_active_lesson'),
    path('get-for-assign/', views.get_data_for_activity, name='get_data_for_activity'),
    path('assign/', views.assign_activity, name='assign_activity'),
    path('mark-as-done/<int:lesson_id>/', views.mark_as_done),
]
