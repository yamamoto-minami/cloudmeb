# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0004_auto_20150722_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='value_input',
            field=models.ForeignKey(related_name='values', null=True, to='inputs.Input', verbose_name='input', blank=True),
        ),
    ]
