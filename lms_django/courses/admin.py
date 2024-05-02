from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'clamped_title', 'created_by', 'status' ]
    list_display_links= ['id', 'clamped_title']
    readonly_fields=['created_at']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'course', 'status', 'lesson_type' ]
    list_display_links= ['id', 'title']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'lesson']
    list_display_links= ['id', 'question']

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Quiz,  QuizAdmin)

