# Generated by Django 2.2.10 on 2020-06-18 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0005_auto_20200618_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matches',
            old_name='current_user',
            new_name='match_users',
        ),
    ]
