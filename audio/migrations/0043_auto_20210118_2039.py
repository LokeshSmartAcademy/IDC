# Generated by Django 3.1.3 on 2021-01-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0042_auto_20210118_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmarks',
            name='POOT_g1',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POOT_g2',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POOT_g3',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POOT_g4',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POOT_g5',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POOT_g6',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POST_g1',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POST_g2',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POST_g3',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POST_g4',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POST_g5',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POST_g6',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POT_g1',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POT_g2',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POT_g3',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POT_g4',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POT_g5',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='POT_g6',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='PRE_g1',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='PRE_g2',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='PRE_g3',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='PRE_g4',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='PRE_g5',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AddField(
            model_name='testmarks',
            name='PRE_g6',
            field=models.CharField(default='-', max_length=2),
        ),
        migrations.AlterField(
            model_name='testschedule',
            name='test_nickname',
            field=models.CharField(default='Al1', max_length=5),
        ),
    ]
