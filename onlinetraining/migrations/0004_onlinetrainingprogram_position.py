# Generated by Django 2.0.2 on 2021-01-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetraining', '0003_auto_20200827_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinetrainingprogram',
            name='Position',
            field=models.IntegerField(default=1),
        ),
    ]