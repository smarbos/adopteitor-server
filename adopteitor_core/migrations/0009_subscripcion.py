# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0008_animal_ubicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscripcion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=255)),
                ('external_reference', models.CharField(max_length=255)),
                ('transaction_amount', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Subscripciones',
            },
        ),
    ]
