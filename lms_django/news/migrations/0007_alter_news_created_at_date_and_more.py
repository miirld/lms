# Generated by Django 5.0.3 on 2024-04-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_rename_created_at_news_created_at_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at_date',
            field=models.DateField(verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at_datetime',
            field=models.DateTimeField(verbose_name='Дата и время создания'),
        ),
    ]