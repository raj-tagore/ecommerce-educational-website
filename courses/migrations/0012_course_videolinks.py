# Generated by Django 2.0.2 on 2020-09-01 00:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20200717_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='VideoLinks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=30),
        ),
    ]