# Generated by Django 4.2.1 on 2023-09-21 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_gsk_delete_mkr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gsk',
            old_name='Event_ID',
            new_name='Patient_Bill',
        ),
        migrations.RenameField(
            model_name='gsk',
            old_name='Event_cost',
            new_name='Patient_ID',
        ),
        migrations.RenameField(
            model_name='gsk',
            old_name='Event_address',
            new_name='Patient_address',
        ),
        migrations.RenameField(
            model_name='gsk',
            old_name='Event_name',
            new_name='Patient_name',
        ),
    ]