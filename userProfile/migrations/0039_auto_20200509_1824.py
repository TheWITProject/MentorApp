# Generated by Django 2.2.10 on 2020-05-09 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0038_auto_20200509_1821'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FrequentlyAskedQ',
            new_name='FrequentlyAsked',
        ),
    ]