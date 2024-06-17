from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'clamped_content', 'created_by', 'type',  'status', 'created_at']
    list_display_links= ['id', 'clamped_content']
    list_filter = ['type', 'status','created_by']


admin.site.register(News, NewsAdmin)
