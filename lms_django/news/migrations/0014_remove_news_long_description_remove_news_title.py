# Generated by Django 5.0.3 on 2024-04-24 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_remove_news_short_description_news_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='long_description',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title',
        ),
    ]