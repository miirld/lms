from django.contrib import admin

from .models import *

class StudyGroupInline (admin.StackedInline):
    model = StudyGroup
    show_change_link = True
    extra = 1

class SchoolAdmin (admin.ModelAdmin):
    list_display = ['id','short_name', 'address']
    list_display_links = ['id', 'short_name']
    inlines = [StudyGroupInline, ]

class StudyGroupAdmin (admin.ModelAdmin):
    list_display = ['id', 'grade', 'letter', 'school', 'entrance_year', 'graduation_year', 'is_active']
    list_display_links = ['id', 'grade', 'letter']
    list_filter = ['school']
    

admin.site.register(StudyGroup, StudyGroupAdmin)

admin.site.register(School, SchoolAdmin)
