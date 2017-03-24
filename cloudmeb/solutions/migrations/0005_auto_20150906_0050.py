# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0004_auto_20150730_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution_values',
            field=models.ManyToManyField(to='values.Value', verbose_name='values', blank=True),
        ),
    ]
