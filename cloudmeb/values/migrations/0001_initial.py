# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('value_id', models.AutoField(primary_key=True, serialize=False)),
                ('value_type', models.CharField(verbose_name='type', max_length=100, choices=[('STRING', 'String'), ('INTEGER', 'Integer'), ('BOOLEAN', 'Boolean'), ('WILDCARD', 'Wildcard')])),
                ('value_name_en', models.CharField(verbose_name='english name', max_length=200)),
                ('value_name_fr', models.CharField(verbose_name='french name', max_length=200)),
                ('value_input', models.ForeignKey(verbose_name='input', blank=True, null=True, to='inputs.Input')),
                ('value_related_value', models.ForeignKey(verbose_name='related value', blank=True, null=True, to='values.Value')),
            ],
            options={
                'verbose_name': 'value',
                'verbose_name_plural': 'values',
            },
        ),
    ]
