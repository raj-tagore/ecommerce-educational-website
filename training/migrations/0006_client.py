# Generated by Django 3.0.1 on 2020-05-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20200517_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=70)),
                ('Phone', models.BigIntegerField(default=9898989898)),
                ('CorpName', models.CharField(default='null', max_length=100)),
                ('Position', models.CharField(default='null', max_length=100)),
                ('Subject', models.TextField(default='null')),
            ],
        ),
    ]
