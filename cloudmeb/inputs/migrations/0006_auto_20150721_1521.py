# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0005_input_input_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='input_salsesforce_id',
        ),
        migrations.AddField(
            model_name='input',
            name='input_salesforce_id',
            field=models.CharField(blank=True, null=True, verbose_name='salesforce id', max_length=50),
        ),
    ]
