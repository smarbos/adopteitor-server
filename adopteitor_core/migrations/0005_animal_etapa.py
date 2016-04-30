# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0004_auto_20160326_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='etapa',
            field=models.CharField(default='a', max_length=1, choices=[(b'c', b'cachorro'), (b'a', b'adulto')]),
            preserve_default=False,
        ),
    ]
