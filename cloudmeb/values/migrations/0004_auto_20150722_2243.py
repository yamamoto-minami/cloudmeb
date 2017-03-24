# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0003_value_value_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='value_input',
            field=models.ForeignKey(to='inputs.Input', verbose_name='input', null=True, related_name='asd', blank=True),
        ),
    ]
