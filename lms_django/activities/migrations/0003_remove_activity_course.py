# Generated by Django 5.0.3 on 2024-06-09 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_alter_activity_participant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='course',
        ),
    ]
