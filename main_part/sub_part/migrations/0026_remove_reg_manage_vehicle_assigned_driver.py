# Generated by Django 3.2.3 on 2021-06-23 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0025_auto_20210623_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg_manage_vehicle',
            name='Assigned_Driver',
        ),
    ]
