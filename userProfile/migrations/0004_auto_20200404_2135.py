# Generated by Django 2.2.10 on 2020-04-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0003_auto_20200404_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='funfact',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(default='', max_length=60),
        ),
    ]
