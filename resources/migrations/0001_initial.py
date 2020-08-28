# Generated by Django 2.0.2 on 2020-08-28 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AUDResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Brief', models.CharField(default='Max 200 characters', max_length=200)),
                ('About', models.TextField(default='null')),
                ('File', models.FileField(default='null', upload_to='Resources/ResourceFiles/')),
                ('FrontPic', models.ImageField(default='null', upload_to='Products/FrontPics/')),
                ('Tags', models.TextField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='JPGResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Brief', models.CharField(default='Max 200 characters', max_length=200)),
                ('About', models.TextField(default='null')),
                ('File', models.FileField(default='null', upload_to='Resources/ResourceFiles/')),
                ('FrontPic', models.ImageField(default='null', upload_to='Products/FrontPics/')),
                ('Tags', models.TextField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='OtherResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Brief', models.CharField(default='Max 200 characters', max_length=200)),
                ('About', models.TextField(default='null')),
                ('File', models.FileField(default='null', upload_to='Resources/ResourceFiles/')),
                ('FrontPic', models.ImageField(default='null', upload_to='Products/FrontPics/')),
                ('Tags', models.TextField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='PDFResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Brief', models.CharField(default='Max 200 characters', max_length=200)),
                ('About', models.TextField(default='null')),
                ('File', models.FileField(default='null', upload_to='Resources/ResourceFiles/')),
                ('FrontPic', models.ImageField(default='null', upload_to='Products/FrontPics/')),
                ('Tags', models.TextField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='PPTResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Brief', models.CharField(default='Max 200 characters', max_length=200)),
                ('About', models.TextField(default='null')),
                ('File', models.FileField(default='null', upload_to='Resources/ResourceFiles/')),
                ('FrontPic', models.ImageField(default='null', upload_to='Products/FrontPics/')),
                ('Tags', models.TextField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='VIDResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Brief', models.CharField(default='Max 200 characters', max_length=200)),
                ('About', models.TextField(default='null')),
                ('File', models.FileField(default='null', upload_to='Resources/ResourceFiles/')),
                ('FrontPic', models.ImageField(default='null', upload_to='Products/FrontPics/')),
                ('Tags', models.TextField(default='null')),
            ],
        ),
    ]
