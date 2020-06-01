# Generated by Django 2.2.10 on 2020-05-04 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0034_auto_20200504_1822'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FrequentlyAskedMentee',
        ),
        migrations.AlterModelOptions(
            name='frequentlyasked',
            options={'verbose_name_plural': 'Frequently Asked Questions'},
        ),
        migrations.RenameField(
            model_name='frequentlyasked',
            old_name='mentor_answer',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='frequentlyasked',
            old_name='mentor_question',
            new_name='question',
        ),
    ]