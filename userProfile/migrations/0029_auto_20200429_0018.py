# Generated by Django 2.2.10 on 2020-04-29 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0028_merge_20200428_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Additional Questions',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=1000)),
                ('order', models.IntegerField(default=0)),
                ('question_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.AdditionalQuestions')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userProfile.Answer')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userProfile.Question')),
                ('question_form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userProfile.AdditionalQuestions')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userProfile.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.Question'),
        ),
        migrations.AddField(
            model_name='profile',
            name='question_form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userProfile.AdditionalQuestions'),
        ),
    ]
