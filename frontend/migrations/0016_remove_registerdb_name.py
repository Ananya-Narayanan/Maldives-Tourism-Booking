# Generated by Django 4.2.6 on 2023-12-17 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0015_booking_details_hoteldb_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerdb',
            name='Name',
        ),
    ]