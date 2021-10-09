# Generated by Django 3.2.8 on 2021-10-09 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout_folders', '0003_auto_20211009_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutexercises',
            name='exercise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workout_folders.exercise'),
        ),
        migrations.AlterField(
            model_name='workoutexercises',
            name='workout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workout_folders.workout'),
        ),
    ]
