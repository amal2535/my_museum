# Generated by Django 4.1.4 on 2023-01-20 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_city_country_alter_room_location_person_city_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
