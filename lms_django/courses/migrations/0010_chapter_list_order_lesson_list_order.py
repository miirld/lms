# Generated by Django 5.0.3 on 2024-05-31 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_course_created_for_alter_course_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='list_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lesson',
            name='list_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
