# Generated by Django 2.1.1 on 2018-09-13 18:52

from django.db import migrations, models
import showcase.models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_auto_20180913_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, help_text='Used for illustration.', upload_to=showcase.models.image_upload_to_dispatcher, verbose_name='image'),
        ),
    ]
