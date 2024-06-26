# Generated by Django 5.0.3 on 2024-05-06 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_created_at_alter_quiz_lesson_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='courses.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Глава',
                'verbose_name_plural': 'Главы',
            },
        ),
    ]
