from django.contrib import admin

from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'lesson',  'participant', 'created_by', 'status' ]
    list_display_links= ['id']
    list_filter = ['course', 'lesson',  'participant', 'created_by']


admin.site.register(Activity, ActivityAdmin)
