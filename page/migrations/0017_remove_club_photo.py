# Generated by Django 2.0.4 on 2018-04-28 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0016_auto_20180428_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='photo',
        ),
    ]