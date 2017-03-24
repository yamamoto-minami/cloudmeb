# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('price_id', models.AutoField(primary_key=True, serialize=False)),
                ('price_name', models.CharField(verbose_name='name', max_length=60, unique=True)),
                ('price_frequency', models.CharField(verbose_name='billing frequency', max_length=100, choices=[('ONE_TIME', 'One time'), ('MONTHLY', 'Monthly'), ('QUARTERLY', 'Quarterly'), ('SEMI_ANNUAL', 'Semi anual'), ('ANNUAL', 'Annual')])),
                ('price_currency', models.CharField(verbose_name='billing currency', max_length=100, choices=[('USD', 'US dollar'), ('CAD', 'Canadian dollar')])),
                ('price_formula', models.TextField(verbose_name='formula', default='0')),
                ('price_inputs', models.ManyToManyField(verbose_name='inputs', blank=True, to='inputs.Input')),
            ],
            options={
                'verbose_name': 'price',
                'verbose_name_plural': 'Prices',
            },
        ),
    ]
