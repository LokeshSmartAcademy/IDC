# Generated by Django 3.1.3 on 2020-12-26 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0005_auto_20201226_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictationaudio',
            old_name='name',
            new_name='audio_name',
        ),
        migrations.RenameField(
            model_name='dictationaudio',
            old_name='path',
            new_name='audio_path',
        ),
    ]
