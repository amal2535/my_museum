# Generated by Django 4.1.4 on 2023-01-23 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_delete_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='likes',
        ),
    ]
