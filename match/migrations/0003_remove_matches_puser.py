# Generated by Django 2.2.10 on 2020-06-13 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_matches_puser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='puser',
        ),
    ]