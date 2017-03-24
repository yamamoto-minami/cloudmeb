# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0004_website_facebook_admin_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='personal_google_plus_url',
            field=models.URLField(default=1, verbose_name='personal google plus id'),
            preserve_default=False,
        ),
    ]
