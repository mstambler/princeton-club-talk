# Generated by Django 2.0.4 on 2018-05-13 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0043_auto_20180512_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
