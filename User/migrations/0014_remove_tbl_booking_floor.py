# Generated by Django 5.0.2 on 2024-04-03 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0013_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_booking',
            name='floor',
        ),
    ]
