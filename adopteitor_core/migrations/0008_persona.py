# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('adopteitor_core', '0007_animal_etapa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('ciudad', models.CharField(max_length=255, choices=[(b'C.A.B.A.', b'C.A.B.A.'), (b'La Plata', b'La Plata'), (b'Mar del Plata', b'Mar del Plata'), (b'Mechonge', b'Mechonge')])),
            ],
        ),
    ]
