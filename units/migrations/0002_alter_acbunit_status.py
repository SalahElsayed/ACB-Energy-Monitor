# Generated by Django 5.1.2 on 2024-10-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acbunit',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=20),
        ),
    ]