# Generated by Django 2.2.10 on 2020-06-13 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0065_remove_response_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userProfile.Answer'),
        ),
    ]
