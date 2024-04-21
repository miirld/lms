# Generated by Django 5.0.3 on 2024-04-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_groups', '0003_remove_school_name_school_full_name_and_more'),
        ('users', '0009_rename_studygroup_customuser_studygroups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='studygroups',
            field=models.ManyToManyField(blank=True, related_name='members', to='study_groups.studygroup', verbose_name='Класс'),
        ),
    ]