# Generated by Django 2.2.10 on 2020-05-04 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0033_auto_20200504_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frequentlyasked',
            old_name='answer',
            new_name='mentor_answer',
        ),
        migrations.RenameField(
            model_name='frequentlyasked',
            old_name='question',
            new_name='mentor_question',
        ),
        migrations.RenameField(
            model_name='frequentlyaskedmentee',
            old_name='answer',
            new_name='mentee_answer',
        ),
        migrations.RenameField(
            model_name='frequentlyaskedmentee',
            old_name='question',
            new_name='mentee_question',
        ),
    ]