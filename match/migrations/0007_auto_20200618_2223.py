# Generated by Django 2.2.10 on 2020-06-18 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0006_matches_match_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='match_profile',
        ),
        migrations.AddField(
            model_name='matches',
            name='manual_match',
            field=models.BooleanField(default=False),
        ),
    ]
