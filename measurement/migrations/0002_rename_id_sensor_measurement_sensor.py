# Generated by Django 3.2.18 on 2023-05-21 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='id_sensor',
            new_name='sensor',
        ),
    ]