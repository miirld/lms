# Generated by Django 5.0.3 on 2024-04-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options_alter_news_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news', verbose_name='Изображение'),
        ),
    ]
