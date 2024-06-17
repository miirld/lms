from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .models import CustomUser

fields = list(UserAdmin.fieldsets)
fields[1] = ('Информация', {'fields':
             ('first_name', 'last_name', 'patronymic', 'email','avatar', 'role','study_groups')})
UserAdmin.fieldsets = tuple(fields)


UserAdmin.list_filter = ('role', 'study_groups', 'is_staff', 'is_superuser', 'is_active', 'groups', )
UserAdmin.list_display = ('username', 'first_name', 'last_name', 'patronymic', 'role', 'is_staff', 'is_superuser', 'is_active' )
UserAdmin.list_display_links = ('username', 'first_name', 'last_name', 'patronymic' )
admin.site.register(CustomUser, UserAdmin)
