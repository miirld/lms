# Generated by Django 5.0.3 on 2024-04-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='short_description',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
