# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('seo_id', models.AutoField(primary_key=True, serialize=False)),
                ('seo_meta_title_en', models.CharField(verbose_name='english meta title', max_length=60, unique=True)),
                ('seo_meta_title_fr', models.CharField(verbose_name='french meta title', max_length=60, unique=True)),
                ('seo_meta_description_en', models.CharField(verbose_name='english meta description', max_length=155, unique=True)),
                ('seo_meta_description_fr', models.CharField(verbose_name='french meta description', max_length=155, unique=True)),
                ('seo_meta_keywords_en', models.CharField(verbose_name='english meta keywords', max_length=1000, unique=True)),
                ('seo_meta_keywords_fr', models.CharField(verbose_name='french meta keywords', max_length=1000, unique=True)),
            ],
            options={
                'verbose_name': 'seo',
                'verbose_name_plural': 'seos',
            },
        ),
    ]
