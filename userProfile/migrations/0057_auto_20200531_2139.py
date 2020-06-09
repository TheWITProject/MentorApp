# Generated by Django 2.2.10 on 2020-05-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0056_auto_20200531_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='bcc_email_mentees',
            field=models.BooleanField(default=False, verbose_name='BCC All Mentees'),
        ),
        migrations.AlterField(
            model_name='email',
            name='bcc_email_mentors',
            field=models.BooleanField(default=False, verbose_name='BCC All Mentors'),
        ),
        migrations.AlterField(
            model_name='email',
            name='bcc_to_email',
            field=models.CharField(blank=True, default='', max_length=1000, verbose_name='BCC:'),
        ),
        migrations.AlterField(
            model_name='email',
            name='cc_email_mentees',
            field=models.BooleanField(default=False, verbose_name='CC All Mentees'),
        ),
        migrations.AlterField(
            model_name='email',
            name='cc_email_mentors',
            field=models.BooleanField(default=False, verbose_name='CC All Mentors'),
        ),
    ]