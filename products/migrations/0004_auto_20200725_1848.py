# Generated by Django 2.0.2 on 2020-07-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_brief'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Brief',
            field=models.CharField(default='Max 200 characters', max_length=200),
        ),
    ]