from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'clamped_content', 'status', 'created_at' ]
    list_display_links= ['id', 'clamped_content']


admin.site.register(News, NewsAdmin)
