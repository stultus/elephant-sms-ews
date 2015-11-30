# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informer',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name of the informer')),
                ('phone', models.CharField(max_length=10, serialize=False, verbose_name='Phone Number of the informer', primary_key=True)),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Adress of the informer', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Siting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=200, verbose_name='Geographic-cordinates of the sitings')),
                ('message', models.CharField(max_length=200, verbose_name='Additional Information')),
                ('informer', models.OneToOneField(to='reports.Informer')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Name of the subscriber', blank=True)),
                ('phone', models.CharField(max_length=10, verbose_name='Phone Number of the subscriber')),
            ],
        ),
    ]
