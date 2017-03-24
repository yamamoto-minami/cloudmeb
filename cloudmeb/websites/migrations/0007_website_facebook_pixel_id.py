# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0006_website_bing_analytics_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='facebook_pixel_id',
            field=models.CharField(verbose_name='facebook pixel id', default=1, max_length=255),
            preserve_default=False,
        ),
    ]
