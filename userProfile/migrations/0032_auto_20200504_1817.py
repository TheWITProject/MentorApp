# Generated by Django 2.2.10 on 2020-05-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0031_auto_20200503_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentlyAskedMentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=1000)),
                ('answer', models.TextField(default='', max_length=5000)),
            ],
            options={
                'verbose_name_plural': 'Frequently Asked Questions Mentor',
            },
        ),
        migrations.RenameModel(
            old_name='FrequentlyAsked',
            new_name='FrequentlyAskedMentee',
        ),
        migrations.AlterModelOptions(
            name='frequentlyaskedmentee',
            options={'verbose_name_plural': 'Frequently Asked Questions Mentee'},
        ),
    ]
