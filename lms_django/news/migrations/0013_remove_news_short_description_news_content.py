# Generated by Django 5.0.3 on 2024-04-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_rename_created_for_group_news_created_for_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='short_description',
        ),
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(default='Это тестовая новость', verbose_name='Текст'),
            preserve_default=False,
        ),
    ]