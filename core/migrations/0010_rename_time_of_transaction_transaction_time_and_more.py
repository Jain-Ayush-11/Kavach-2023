# Generated by Django 4.2.4 on 2023-08-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_websitereport_socialmedia_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='time_of_transaction',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='address',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='block_height',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='previous_report',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='recipient_address',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='sender_address',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='type_of_blockchain',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='type_of_event',
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='logo',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='reciever_amount',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='reciever_to',
            field=models.CharField(blank=True, max_length=34, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender',
            field=models.CharField(blank=True, max_length=34, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transactionHash',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
