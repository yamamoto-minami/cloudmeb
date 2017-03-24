# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0004_input_input_salsesforce_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='input_order',
            field=models.IntegerField(null=True, blank=True, verbose_name='order'),
        ),
    ]
