# Generated by Django 3.1.3 on 2021-01-08 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0036_auto_20210108_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmarks',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.studentenroll'),
        ),
    ]
