# Generated by Django 2.0.2 on 2020-08-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0011_auto_20200825_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingprogram',
            name='DaywiseSchedule',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='trainingprogram',
            name='FreeMaterials',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='trainingprogram',
            name='SpecialAttractions',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='trainingprogram',
            name='WhatYouWillLearn',
            field=models.TextField(default='null'),
        ),
    ]