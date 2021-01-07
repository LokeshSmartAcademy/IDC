# Generated by Django 3.1.3 on 2020-12-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCardDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_number', models.CharField(max_length=100)),
                ('level_image', models.ImageField(upload_to='pics')),
                ('level_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('level_desc', models.CharField(max_length=500)),
            ],
        ),
    ]
