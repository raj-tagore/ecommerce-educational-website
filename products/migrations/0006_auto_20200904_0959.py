# Generated by Django 2.0.2 on 2020-09-04 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200728_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='BasePrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='DeliveryCharges',
            field=models.IntegerField(default=0),
        ),
    ]