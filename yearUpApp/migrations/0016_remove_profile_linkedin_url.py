# Generated by Django 2.2.10 on 2020-04-04 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearUpApp', '0015_auto_20200404_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='linkedin_url',
        ),
    ]
