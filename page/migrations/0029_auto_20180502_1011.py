# Generated by Django 2.0.4 on 2018-05-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0028_auto_20180501_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
