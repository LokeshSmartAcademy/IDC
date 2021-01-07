# Generated by Django 3.1.3 on 2020-12-29 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0009_studentenroll_stusubject'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=20)),
                ('scheduled_date', models.DateField()),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('showthis', models.BooleanField(default=True)),
            ],
        ),
    ]
