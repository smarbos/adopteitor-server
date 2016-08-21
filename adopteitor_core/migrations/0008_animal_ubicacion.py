# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0007_animal_etapa'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='ubicacion',
            field=models.CharField(default='buenos-aires', max_length=255, choices=[(b'buenos-aires', b'Buenos Aires'), (b'neuquen', b'Neuquen')]),
            preserve_default=False,
        ),
    ]
