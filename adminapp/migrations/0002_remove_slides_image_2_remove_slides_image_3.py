# Generated by Django 4.1.4 on 2023-01-05 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slides',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='slides',
            name='image_3',
        ),
    ]
