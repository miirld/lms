from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_activity_courses, name='get_activity_courses'),
    path('<int:id>/', views.get_active_course),
    # path('progress/', views.get_progress_courses, name='get_progress_courses'),
    path('my-groups/', views.get_my_groups, name='get_my_groups'),
    path('group-progress/<int:group_id>/get-data/', views.get_group_name, name='get_group_name'),
    # path('course-progress/<int:course_id>/groups/', views.get_progress, name='get_progress'),
    path('group-progress/<int:group_id>/', views.get_my_group_progress, name='get_my_group_progress',),
    path('lesson/<int:lesson_id>/', views.get_lesson_status, name='get_active_lesson'),
    path('get-data-to-assign/', views.get_data_for_activity, name='get_data_for_activity'),
    path('assign/', views.assign_activity, name='assign_activity'),
    path('mark-as-done/<int:lesson_id>/', views.mark_as_done),
]
