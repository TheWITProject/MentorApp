# Generated by Django 2.2.10 on 2020-03-30 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearUpApp', '0003_auto_20200330_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=15),
        ),
    ]
