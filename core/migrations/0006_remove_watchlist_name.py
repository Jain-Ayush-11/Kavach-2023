# Generated by Django 4.2.4 on 2023-08-08 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_event_watchlist_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='name',
        ),
    ]
