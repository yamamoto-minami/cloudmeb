# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0002_auto_20150710_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='add_this_id',
            field=models.CharField(verbose_name='add this id', max_length=255, default=1),
            preserve_default=False,
        ),
    ]
