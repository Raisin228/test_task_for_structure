# Generated by Django 5.0.1 on 2024-01-30 17:41

import application1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='any_file',
            name='file',
            field=models.FileField(upload_to=application1.models.user_directory_path_by_files),
        ),
        migrations.AlterField(
            model_name='any_file',
            name='image',
            field=models.ImageField(upload_to=application1.models.user_directory_path_by_images),
        ),
    ]