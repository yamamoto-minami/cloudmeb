# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='facebook_id',
        ),
        migrations.RemoveField(
            model_name='website',
            name='google_plus_id',
        ),
        migrations.RemoveField(
            model_name='website',
            name='linkedin_id',
        ),
        migrations.RemoveField(
            model_name='website',
            name='twitter_id',
        ),
        migrations.AddField(
            model_name='website',
            name='facebook_url',
            field=models.URLField(verbose_name='facebook id', default='http://someurl.com/id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='website',
            name='google_plus_url',
            field=models.URLField(verbose_name='google plus id', default='http://someurl.com/id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='website',
            name='linkedin_url',
            field=models.URLField(verbose_name='linkedin id', default='http://someurl.com/id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='website',
            name='twitter_url',
            field=models.URLField(verbose_name='twitter id', default='http://someurl.com/id'),
            preserve_default=False,
        ),
    ]
