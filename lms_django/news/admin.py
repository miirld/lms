from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_description', 'status' ]
    list_display_links= ['id', 'short_description']


admin.site.register(News, NewsAdmin)
