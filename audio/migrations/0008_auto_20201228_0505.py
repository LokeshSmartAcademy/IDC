# Generated by Django 3.1.3 on 2020-12-28 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0007_studentenroll_stu_isactive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentenroll',
            old_name='stu_isactive',
            new_name='is_active',
        ),
    ]