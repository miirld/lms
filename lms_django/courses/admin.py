from django.contrib import admin
from .models import *


class LessonInline(admin.StackedInline):
    model = Lesson
    show_change_link = True
    extra = 1
    ordering=('chapter__list_order', 'list_order')

class QuizInline(admin.StackedInline):
    model = Quiz
    show_change_link = True
    extra = 1
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links= ['id', 'title']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'clamped_title', 'created_by', 'status' ]
    list_display_links= ['id', 'clamped_title']
    readonly_fields=['created_at']
    inlines = [LessonInline,]

class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'course']
    list_display_links= ['id', 'title']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'course', 'chapter', 'status', 'lesson_type' ]
    list_display_links= ['id', 'title']
    inlines = [QuizInline,]


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'lesson']
    list_display_links= ['id', 'question']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Quiz,  QuizAdmin)
admin.site.register(Chapter, ChapterAdmin)

