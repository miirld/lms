# Generated by Django 5.0.3 on 2024-05-13 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_alter_news_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='created_for',
        ),
    ]