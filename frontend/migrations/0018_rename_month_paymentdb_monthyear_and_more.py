# Generated by Django 4.2.6 on 2023-12-19 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0017_paymentdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentdb',
            old_name='month',
            new_name='monthyear',
        ),
        migrations.RemoveField(
            model_name='paymentdb',
            name='year',
        ),
    ]
