# Generated by Django 2.1.1 on 2018-09-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0004_auto_20180913_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='github_link',
            field=models.URLField(blank=True, default='aurthurm/', help_text='Github link as: username/repository', verbose_name='url'),
        ),
    ]
