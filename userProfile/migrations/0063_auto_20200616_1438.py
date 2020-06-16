# Generated by Django 2.2.10 on 2020-06-16 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0062_merge_20200616_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.Question'),
        ),
        migrations.AlterField(
            model_name='response',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userProfile.Answer'),
        ),
    ]
