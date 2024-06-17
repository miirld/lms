from django.contrib import admin

from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'lesson', 'created_by',  'participant',  'status' ]
    list_display_links= ['id']
    list_filter = ['status', 'created_by', 'participant', 'lesson__chapter__course',  'lesson',   ]


admin.site.register(Activity, ActivityAdmin)
