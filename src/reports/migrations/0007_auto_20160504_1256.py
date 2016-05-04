# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_siting_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='grids',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='siting',
            name='picture',
            field=models.ImageField(upload_to='siting_pics/%Y-%m-%d/', null=True, verbose_name='Picture', blank=True),
        ),
    ]
