# Generated by Django 5.0.3 on 2024-05-13 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_groups', '0005_studygroup_tutors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studygroup',
            name='teachers',
        ),
        migrations.RemoveField(
            model_name='studygroup',
            name='tutors',
        ),
    ]