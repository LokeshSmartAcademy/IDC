# Generated by Django 3.1.3 on 2020-12-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuname', models.CharField(max_length=30)),
                ('stuclass', models.CharField(max_length=10)),
                ('stuschool', models.CharField(max_length=40)),
                ('stutown', models.CharField(max_length=30)),
                ('stucontact', models.CharField(max_length=12)),
                ('stuemail', models.EmailField(max_length=254)),
            ],
        ),
    ]
