# Generated by Django 3.2.8 on 2021-10-21 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasts', '0002_alter_fasts_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fasts',
            name='end',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fasts',
            name='start',
            field=models.DateTimeField(),
        ),
    ]