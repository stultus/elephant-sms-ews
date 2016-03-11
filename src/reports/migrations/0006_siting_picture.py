# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20160311_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='siting',
            name='picture',
            field=models.ImageField(upload_to='siting_pics/%Y-%m-%d/', null=True, verbose_name='Profile picture', blank=True),
        ),
    ]
