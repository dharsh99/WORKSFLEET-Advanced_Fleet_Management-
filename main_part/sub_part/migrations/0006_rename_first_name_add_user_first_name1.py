# Generated by Django 3.2.3 on 2021-06-13 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0005_add_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_user',
            old_name='first_name',
            new_name='first_name1',
        ),
    ]
