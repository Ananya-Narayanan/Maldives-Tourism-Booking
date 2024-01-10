# Generated by Django 4.2.6 on 2023-11-27 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_spadb_idimage_spadb_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spadb',
            name='idimage',
        ),
        migrations.AddField(
            model_name='spadb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='id_image'),
        ),
    ]