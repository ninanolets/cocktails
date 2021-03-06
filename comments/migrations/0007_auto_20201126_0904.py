# Generated by Django 3.1.2 on 2020-11-26 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_auto_20201117_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='update_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
