# Generated by Django 5.0.3 on 2024-06-09 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_course_image_alter_lesson_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='lesson',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='courses.lesson', verbose_name='Урок'),
        ),
    ]