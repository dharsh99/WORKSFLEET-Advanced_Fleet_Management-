# Generated by Django 3.2.3 on 2021-06-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_admin_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Signin_Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
