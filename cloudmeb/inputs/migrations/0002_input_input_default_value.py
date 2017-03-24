# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0001_initial'),
        ('inputs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='input_default_value',
            field=models.ForeignKey(verbose_name='default value', blank=True, null=True, to='values.Value'),
        ),
    ]
