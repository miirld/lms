from django.urls import path
from courses import views

urlpatterns = [
    path('', views.get_courses),
    path('categories/', views.get_categories),
    path('<int:id>/', views.get_course),
    path('<int:course_id>/<int:lesson_id>/get-quiz/', views.get_quiz),
]

