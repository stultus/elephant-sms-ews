# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20151016_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='siting',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 11, 14, 42, 982493, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='grids',
            field=models.CharField(max_length=1000, null=True, verbose_name='Comma sperated grid numbers to get alerts'),
        ),
        migrations.AlterField(
            model_name='siting',
            name='message',
            field=models.CharField(max_length=200, null=True, verbose_name='Additional Information', blank=True),
        ),
    ]
