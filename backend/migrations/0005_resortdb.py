# Generated by Django 4.2.6 on 2023-11-05 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_roomtype_roomdb_nights'),
    ]

    operations = [
        migrations.CreateModel(
            name='resortdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResortName', models.CharField(blank=True, max_length=20, null=True)),
                ('Hour', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='resortimage')),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
