# Generated by Django 4.1.5 on 2023-02-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_human_element'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Изображение'),
        ),
    ]
