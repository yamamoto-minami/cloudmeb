# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0007_website_facebook_pixel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='hotjar_id',
            field=models.CharField(default=1, verbose_name='hotjar id', max_length=255),
            preserve_default=False,
        ),
    ]
