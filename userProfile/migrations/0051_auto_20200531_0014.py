# Generated by Django 2.2.10 on 2020-05-31 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0050_auto_20200530_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='bcc_to_email',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='email',
            name='cc_to_email',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='email',
            name='to_email',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
