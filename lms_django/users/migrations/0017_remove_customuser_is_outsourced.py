# Generated by Django 5.0.3 on 2024-05-31 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_customuser_is_outsourced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_outsourced',
        ),
    ]