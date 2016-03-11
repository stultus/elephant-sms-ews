# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='siting',
            name='herd_id',
            field=models.CharField(max_length=200, null=True, verbose_name='Herd Id', blank=True),
        ),
        migrations.AlterField(
            model_name='siting',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
