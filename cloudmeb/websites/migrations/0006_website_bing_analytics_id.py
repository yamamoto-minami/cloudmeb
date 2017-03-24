# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0005_website_personal_google_plus_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='bing_analytics_id',
            field=models.CharField(default=1, max_length=255, verbose_name='bing analytics id'),
            preserve_default=False,
        ),
    ]
