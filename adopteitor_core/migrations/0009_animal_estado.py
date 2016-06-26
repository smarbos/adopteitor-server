# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0008_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='estado',
            field=models.CharField(default=1, max_length=1, choices=[(b'1', b'En adopcion'), (b'2', b'En Transito'), (b'3', b'Adoptado')]),
            preserve_default=False,
        ),
    ]
