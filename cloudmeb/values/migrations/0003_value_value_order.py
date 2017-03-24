# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0002_value_value_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='value_order',
            field=models.IntegerField(null=True, blank=True, verbose_name='order'),
        ),
    ]
