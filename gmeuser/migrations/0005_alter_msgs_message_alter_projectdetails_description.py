# Generated by Django 4.1.4 on 2023-01-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmeuser', '0004_msgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='Message',
            field=models.CharField(max_length=50000),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='description',
            field=models.CharField(max_length=10000),
        ),
    ]