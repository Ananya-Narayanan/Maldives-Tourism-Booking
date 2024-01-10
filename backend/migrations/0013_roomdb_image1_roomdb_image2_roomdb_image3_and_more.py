# Generated by Django 4.2.6 on 2023-11-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_remove_roomdb_roomimage_alter_roomdb_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomdb',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='roomimage1'),
        ),
        migrations.AddField(
            model_name='roomdb',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='roomimage2'),
        ),
        migrations.AddField(
            model_name='roomdb',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='roomimage3'),
        ),
        migrations.AlterField(
            model_name='roomdb',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
