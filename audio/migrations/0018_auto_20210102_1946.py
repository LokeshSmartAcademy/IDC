# Generated by Django 3.1.3 on 2021-01-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0017_auto_20210102_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentteststats',
            name='examconducted',
            field=models.CharField(default='TESTTS', max_length=10),
        ),
    ]