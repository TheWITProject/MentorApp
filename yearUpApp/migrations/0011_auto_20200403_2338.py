# Generated by Django 2.2.10 on 2020-04-03 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearUpApp', '0010_auto_20200403_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
