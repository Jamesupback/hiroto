# Generated by Django 5.0.2 on 2024-03-19 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0003_tbl_facility'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_roomtype',
            old_name='room_type',
            new_name='roomtype_type',
        ),
    ]
