# Generated by Django 3.2.3 on 2021-06-25 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0032_auto_20210625_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg_vehicle_group',
            name='Is_Enable',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
