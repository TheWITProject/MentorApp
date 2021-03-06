# Generated by Django 2.2.10 on 2020-04-25 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0025_auto_20200425_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userProfile.Answer'),
        ),
        migrations.AlterField(
            model_name='response',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userProfile.Question'),
        ),
    ]
