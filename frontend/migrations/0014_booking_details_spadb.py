# Generated by Django 4.2.6 on 2023-12-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_booking_details_hoteldb_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking_details_spadb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spaname', models.CharField(blank=True, max_length=100, null=True)),
                ('spaprice', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]