# Generated by Django 2.0.4 on 2018-05-13 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0041_auto_20180512_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='leader',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
