# Generated by Django 3.1.2 on 2020-11-17 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20201116_2236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['pub_date']},
        ),
    ]
