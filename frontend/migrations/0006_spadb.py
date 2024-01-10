# Generated by Django 4.2.6 on 2023-11-27 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_alter_contactdb_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='spadb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField(blank=True, null=True)),
                ('checkout', models.DateField(blank=True, null=True)),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('adults', models.IntegerField(blank=True, null=True)),
                ('children', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]