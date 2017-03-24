# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0005_auto_20150722_2247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='value',
            options={'verbose_name': 'value', 'verbose_name_plural': 'values', 'ordering': ['value_order']},
        ),
    ]
