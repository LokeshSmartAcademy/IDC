# Generated by Django 3.1.3 on 2021-01-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0040_auto_20210108_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testschedule',
            name='test_type',
            field=models.CharField(choices=[('PRE', 'PRE'), ('POT', 'POT'), ('POOT', 'POOT'), ('POST', 'POST')], max_length=10),
        ),
    ]
