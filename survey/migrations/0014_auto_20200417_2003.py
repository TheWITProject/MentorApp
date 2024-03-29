# Generated by Django 2.2.10 on 2020-04-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_auto_20200417_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'Big Text Box(multiple line)'), ('short-text', 'short text (one line)'), ('radio', 'radio'), ('select', 'select'), ('select-multiple', 'Select Multiple'), ('select_image', 'Select Image'), ('integer', 'integer'), ('float', 'float'), ('date', 'date')], default='text', max_length=200, verbose_name='Type'),
        ),
    ]
