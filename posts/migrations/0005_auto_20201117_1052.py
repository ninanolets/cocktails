# Generated by Django 3.1.2 on 2020-11-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20201116_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sub_title',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
