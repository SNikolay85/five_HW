# Generated by Django 4.2.1 on 2023-05-22 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_remove_measurement_time_measure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor',
            new_name='id_sensor',
        ),
    ]
