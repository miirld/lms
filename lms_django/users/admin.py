from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .models import CustomUser

fields = list(UserAdmin.fieldsets)
fields[1] = ('Личная информация', {'fields':
             ('first_name', 'last_name', 'patronymic', 'email','avatar', 'studygroups')})


UserAdmin.fieldsets = tuple(fields)
admin.site.register(CustomUser, UserAdmin)
