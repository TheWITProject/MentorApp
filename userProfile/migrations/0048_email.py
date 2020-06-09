# Generated by Django 2.2.10 on 2020-05-30 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0047_delete_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_email', models.CharField(default='', max_length=1000)),
                ('from_email', models.CharField(default='', max_length=1000)),
                ('subject', models.CharField(default='', max_length=1000)),
                ('message_email', models.TextField(default='', max_length=5000)),
            ],
        ),
    ]