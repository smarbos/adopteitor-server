# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0002_formularioadopcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioadopcion',
            name='ciudad',
            field=models.CharField(max_length=255, choices=[(b'C.A.B.A.', b'C.A.B.A.'), (b'La Plata', b'La Plata'), (b'Mar del Plata', b'Mar del Plata'), (b'Mechonge', b'Mechonge')]),
        ),
    ]
