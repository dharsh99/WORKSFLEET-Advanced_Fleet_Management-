# Generated by Django 3.2.3 on 2021-06-25 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0031_auto_20210625_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Air_conditioner_working_or_not',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Anyofour_powertools',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Automaticlocks_alarmworking',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Car_mats_Car_seat_covers',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Condition_or_carseats',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Damagetoexterior_ofcarsdents_scratches_brokenlights_etc',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='DateTime_Incomig',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='DateTime_Outgoing',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Extension_leads',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Fuel_level_Incoming',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Fuel_level_outgoing',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Interior_Lights',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Interior_damages',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Inventor_cigerette',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Ladders_extension_ladder',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Light_Indicators',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Lights_headlights_working',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Meter_Reading_Incoming',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Petrol_card',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Suspension',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Tool_boxes',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='TyresNew_need_replacing',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='Windows_working_or_not_anydamages_windowtints',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg_vehicle_inspection',
            name='oil_check',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]