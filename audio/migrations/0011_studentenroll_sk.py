# Generated by Django 3.1.3 on 2020-12-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0010_testschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentenroll',
            name='sk',
            field=models.CharField(default='dummmi', max_length=10),
        ),
    ]
