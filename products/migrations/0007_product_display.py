# Generated by Django 2.0.2 on 2020-09-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200904_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Display',
            field=models.BooleanField(default=True),
        ),
    ]
