# Generated by Django 2.2.10 on 2020-06-18 00:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('match', '0004_matches_puser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='puser',
        ),
        migrations.AddField(
            model_name='matches',
            name='current_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
