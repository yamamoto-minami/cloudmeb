# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0003_website_add_this_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='facebook_admin_id',
            field=models.CharField(default=1, max_length=255, verbose_name='facebook admin id'),
            preserve_default=False,
        ),
    ]
