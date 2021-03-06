# Generated by Django 2.0.2 on 2020-09-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200907_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ActivateDiscount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='DiscountedPrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='Position',
            field=models.IntegerField(default=1),
        ),
    ]
