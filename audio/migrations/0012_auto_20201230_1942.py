# Generated by Django 3.1.3 on 2020-12-30 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0011_studentenroll_sk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testschedule',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.studentenroll'),
        ),
    ]
