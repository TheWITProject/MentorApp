# Generated by Django 2.2.10 on 2020-05-31 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0053_auto_20200531_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email_mentors',
            field=models.BooleanField(default=False, verbose_name='Email All Mentors'),
        ),
    ]
