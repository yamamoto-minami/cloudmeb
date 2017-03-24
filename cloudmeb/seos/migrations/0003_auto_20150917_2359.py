# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seos', '0002_auto_20150710_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo',
            name='seo_image_en',
            field=models.ImageField(upload_to='seos/', verbose_name='english seo image', default='placeholders/300x300.gif'),
        ),
        migrations.AddField(
            model_name='seo',
            name='seo_image_fr',
            field=models.ImageField(upload_to='seos/', verbose_name='french seo image', default='placeholders/300x300.gif'),
        ),
        migrations.AddField(
            model_name='seo',
            name='seo_type',
            field=models.CharField(max_length=100, verbose_name='seo type', default='WEBSITE', choices=[('WEBSITE', 'Website'), ('ARTICLE', 'Article')]),
            preserve_default=False,
        ),
    ]
