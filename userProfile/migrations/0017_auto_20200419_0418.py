# Generated by Django 2.2.10 on 2020-04-19 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0016_auto_20200419_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profileimage.png', null=True, upload_to=''),
        ),
    ]