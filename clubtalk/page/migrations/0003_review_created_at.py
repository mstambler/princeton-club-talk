# Generated by Django 2.0.4 on 2018-04-22 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20180420_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
