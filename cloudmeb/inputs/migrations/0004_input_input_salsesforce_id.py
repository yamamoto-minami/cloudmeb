# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0003_input_input_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='input_salsesforce_id',
            field=models.CharField(verbose_name='salsesforce id', max_length=50, null=True, blank=True),
        ),
    ]
