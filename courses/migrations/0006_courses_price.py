# Generated by Django 2.2.7 on 2020-04-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20200413_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
