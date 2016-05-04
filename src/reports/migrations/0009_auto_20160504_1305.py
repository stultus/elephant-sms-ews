# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20160504_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siting',
            name='is_notified',
            field=models.BooleanField(default=False),
        ),
    ]
