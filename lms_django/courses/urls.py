from django.urls import path
from courses import views

urlpatterns = [
    path('', views.get_courses),
    path('categories/', views.get_categories),
    path('<int:id>/', views.get_course),
    path('lesson/<int:lesson_id>/', views.get_lesson),
    path('lesson/<int:lesson_id>/get-quiz/', views.get_quiz),
]

