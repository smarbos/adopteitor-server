# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0009_animal_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formularioadopcion',
            old_name='galgo',
            new_name='animal',
        ),
    ]
