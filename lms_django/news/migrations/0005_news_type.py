# Generated by Django 5.0.3 on 2024-04-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_created_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='type',
            field=models.CharField(choices=[('article', 'Статья'), ('message', 'Сообщение')], default='article', max_length=25, verbose_name='Тип'),
        ),
    ]
