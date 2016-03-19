# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=1, choices=[(b'm', b'macho'), (b'h', b'hembra')])),
                ('fecha_nacimiento', models.DateTimeField()),
                ('desc', models.TextField(max_length=1024)),
                ('fecha_ingreso', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Animales',
            },
        ),
        migrations.CreateModel(
            name='AnimalFoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'images/', verbose_name=b'File')),
                ('galgo', models.ForeignKey(related_name='fotos', blank=True, to='adopteitor_core.Animal', null=True)),
            ],
        ),
    ]
