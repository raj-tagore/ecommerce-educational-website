# Generated by Django 2.0.2 on 2021-01-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetraining', '0005_onlinetrainingapplicant_coursename'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinetrainingprogram',
            name='MeetingLink',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='onlinetrainingprogram',
            name='StartMeeting',
            field=models.BooleanField(default=False),
        ),
    ]