# Generated by Django 4.2.4 on 2023-11-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusStopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatch',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
