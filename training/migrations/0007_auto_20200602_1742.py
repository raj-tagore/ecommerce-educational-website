# Generated by Django 2.0.2 on 2020-06-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingapplicants',
            name='Course',
        ),
        migrations.AddField(
            model_name='trainingapplicants',
            name='CourseId',
            field=models.IntegerField(default=0),
        ),
    ]
