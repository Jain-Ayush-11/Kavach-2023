# Generated by Django 4.2.4 on 2023-08-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_socialmedia_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True, unique=True)),
                ('report_id', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='address',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
