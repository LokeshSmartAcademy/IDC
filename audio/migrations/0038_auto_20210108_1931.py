# Generated by Django 3.1.3 on 2021-01-08 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0037_auto_20210108_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmarks',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='audio.studentenroll'),
        ),
    ]
