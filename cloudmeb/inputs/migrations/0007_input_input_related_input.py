# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0006_auto_20150721_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='input_related_input',
            field=models.ForeignKey(blank=True, verbose_name='related input', null=True, to='inputs.Input'),
        ),
    ]
