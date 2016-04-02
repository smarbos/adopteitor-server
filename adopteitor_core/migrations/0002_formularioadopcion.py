# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioAdopcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('ciudad', models.CharField(max_length=255, choices=[(1, b'C.A.B.A.'), (2, b'La Plata'), (3, b'Mar del Plata'), (4, b'Mechonge')])),
                ('galgo', models.ForeignKey(related_name='formularios', blank=True, to='adopteitor_core.Animal', null=True)),
            ],
        ),
    ]
