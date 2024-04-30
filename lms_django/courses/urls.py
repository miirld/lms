from django.urls import path
from courses import views

urlpatterns = [
    path('', views.get_courses),
    path('categories/', views.get_categories),
]