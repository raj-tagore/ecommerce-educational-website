# Generated by Django 2.2.7 on 2020-04-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('videofile1', models.FileField(null=True, upload_to='videos/')),
                ('videofile2', models.FileField(null=True, upload_to='videos/')),
                ('videofile3', models.FileField(null=True, upload_to='videos/')),
                ('videofile4', models.FileField(null=True, upload_to='videos/')),
                ('videofile5', models.FileField(null=True, upload_to='videos/')),
                ('videofile6', models.FileField(null=True, upload_to='videos/')),
                ('videofile7', models.FileField(null=True, upload_to='videos/')),
                ('videofile8', models.FileField(null=True, upload_to='videos/')),
                ('videofile9', models.FileField(null=True, upload_to='videos/')),
                ('videofile10', models.FileField(null=True, upload_to='videos/')),
                ('videofile11', models.FileField(null=True, upload_to='videos/')),
                ('videofile12', models.FileField(null=True, upload_to='videos/')),
                ('videofile13', models.FileField(null=True, upload_to='videos/')),
                ('videofile14', models.FileField(null=True, upload_to='videos/')),
                ('videofile15', models.FileField(null=True, upload_to='videos/')),
                ('videofile16', models.FileField(null=True, upload_to='videos/')),
                ('videofile17', models.FileField(null=True, upload_to='videos/')),
                ('videofile18', models.FileField(null=True, upload_to='videos/')),
                ('videofile19', models.FileField(null=True, upload_to='videos/')),
                ('videofile20', models.FileField(null=True, upload_to='videos/')),
                ('videofile21', models.FileField(null=True, upload_to='videos/')),
                ('videofile22', models.FileField(null=True, upload_to='videos/')),
                ('videofile23', models.FileField(null=True, upload_to='videos/')),
                ('videofile24', models.FileField(null=True, upload_to='videos/')),
                ('videofile25', models.FileField(null=True, upload_to='videos/')),
                ('videofile26', models.FileField(null=True, upload_to='videos/')),
                ('videofile27', models.FileField(null=True, upload_to='videos/')),
                ('videofile28', models.FileField(null=True, upload_to='videos/')),
                ('videofile29', models.FileField(null=True, upload_to='videos/')),
                ('videofile30', models.FileField(null=True, upload_to='videos/')),
            ],
        ),
    ]
