# Generated by Django 2.0.2 on 2020-08-27 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetraining', '0002_auto_20200801_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineTrainingApplicantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('About', models.TextField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineTrainingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('About', models.TextField(default='null')),
            ],
        ),
        migrations.AddField(
            model_name='onlinetrainingapplicant',
            name='Address',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='onlinetrainingprogram',
            name='DaywiseSchedule',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='onlinetrainingprogram',
            name='FreeMaterials',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='onlinetrainingprogram',
            name='Language',
            field=models.CharField(default='Hindi', max_length=50),
        ),
        migrations.AddField(
            model_name='onlinetrainingprogram',
            name='SpecialAttractions',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='onlinetrainingprogram',
            name='WhatYouWillLearn',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='onlinetrainingprogram',
            name='ApplicantType',
            field=models.ManyToManyField(to='onlinetraining.OnlineTrainingApplicantType'),
        ),
        migrations.AddField(
            model_name='onlinetrainingprogram',
            name='Category',
            field=models.ManyToManyField(to='onlinetraining.OnlineTrainingCategory'),
        ),
    ]
