# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seos', '0003_auto_20150917_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo',
            name='seo_meta_debug',
            field=models.TextField(verbose_name='debug', default='debug'),
        ),
    ]
