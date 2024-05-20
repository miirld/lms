# Generated by Django 5.0.3 on 2024-05-13 09:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_groups', '0004_studygroup_teachers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroup',
            name='tutors',
            field=models.ManyToManyField(blank=True, related_name='wards_group', to=settings.AUTH_USER_MODEL, verbose_name='Кураторы'),
        ),
    ]