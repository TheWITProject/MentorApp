# Generated by Django 2.2.10 on 2020-04-18 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0011_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
