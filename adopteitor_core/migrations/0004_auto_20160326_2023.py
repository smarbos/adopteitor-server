# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0003_auto_20160325_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioadopcion',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
