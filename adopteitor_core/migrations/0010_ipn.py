# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0009_subscripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ipn',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('content', jsonfield.fields.JSONField()),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Ipns',
            },
        ),
    ]
