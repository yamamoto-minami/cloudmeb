# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='value_value',
            field=models.CharField(max_length=200, blank=True, null=True, verbose_name='value'),
        ),
    ]
