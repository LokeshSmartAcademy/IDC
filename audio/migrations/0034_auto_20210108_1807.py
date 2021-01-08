# Generated by Django 3.1.3 on 2021-01-08 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0033_testschedule_test_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenroll',
            name='stuclass',
            field=models.CharField(choices=[('C1', '1'), ('C2', '2'), ('C3', '3'), ('C4', '4'), ('C5', '5'), ('C6', '6'), ('C7', '7'), ('C8', '8'), ('C9', '9'), ('C10', '10'), ('C_', '_')], max_length=10),
        ),
        migrations.CreateModel(
            name='TestMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l1', models.IntegerField(default=-1)),
                ('l2', models.IntegerField(default=-1)),
                ('l3', models.IntegerField(default=-1)),
                ('l4', models.IntegerField(default=-1)),
                ('l5', models.IntegerField(default=-1)),
                ('l6', models.IntegerField(default=-1)),
                ('l7', models.IntegerField(default=-1)),
                ('l8', models.IntegerField(default=-1)),
                ('l9', models.IntegerField(default=-1)),
                ('l10', models.IntegerField(default=-1)),
                ('l12', models.IntegerField(default=-1)),
                ('l13', models.IntegerField(default=-1)),
                ('l14', models.IntegerField(default=-1)),
                ('l15', models.IntegerField(default=-1)),
                ('l16', models.IntegerField(default=-1)),
                ('l17', models.IntegerField(default=-1)),
                ('l18', models.IntegerField(default=-1)),
                ('l19', models.IntegerField(default=-1)),
                ('l20', models.IntegerField(default=-1)),
                ('l21', models.IntegerField(default=-1)),
                ('l22', models.IntegerField(default=-1)),
                ('l23', models.IntegerField(default=-1)),
                ('l24', models.IntegerField(default=-1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.studentenroll')),
            ],
        ),
    ]
