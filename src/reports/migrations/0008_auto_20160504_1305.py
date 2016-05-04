# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20160504_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='siting',
            name='is_notified',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='location',
            field=models.CharField(max_length=1000, null=True, verbose_name='Location of the subscriber to get alerts'),
        ),
    ]
