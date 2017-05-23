# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0010_ipn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipn',
            options={'verbose_name_plural': 'IpnS'},
        ),
    ]
