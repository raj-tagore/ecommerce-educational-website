# Generated by Django 2.0.2 on 2021-01-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetraining', '0004_onlinetrainingprogram_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinetrainingapplicant',
            name='CourseName',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
