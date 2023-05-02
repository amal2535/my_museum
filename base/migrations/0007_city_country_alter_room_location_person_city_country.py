# Generated by Django 4.1.4 on 2023-01-20 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_room_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='location',
            field=models.CharField(choices=[('Tunis', 'TUNIS'), ('Monastir', 'MONASTIR'), ('Gabes', 'GABES'), ('Medenin', 'MEDENIN'), ('Sousse', 'SOUSSE'), ('Binzert', 'BINZERT'), ('Sfax', 'SFAX'), ('Tozeur', 'TOZEUR'), ('Tataouine', 'TATAOUINE'), ('Mahdia', 'MAHDIA'), ('Kairouan', 'KAIROUAN'), ('BenArous', 'BENAROUS'), ('Gafsa', 'GABES'), ('Jandouba', 'JANDOUBA'), ('El kef', 'ELKEF'), ('Ariana', 'ARIANA'), ('Kasserine', 'KASERINE'), ('SidiBouzid', 'SIDIBOUZID'), ('beja', 'BEJA'), ('Zagouen', 'ZAGOUEN'), ('seliana', 'SELIANA'), ('kebili', 'KEBILI'), ('Manouba', 'MANOUBA'), ('Nabeul', 'NABEUL')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.city')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.country'),
        ),
    ]
