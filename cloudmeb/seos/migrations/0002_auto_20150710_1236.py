# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='seo_meta_description_en',
            field=models.TextField(max_length=155, unique=True, verbose_name='english meta description'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='seo_meta_description_fr',
            field=models.TextField(max_length=155, unique=True, verbose_name='french meta description'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='seo_meta_keywords_en',
            field=models.TextField(max_length=1000, unique=True, verbose_name='english meta keywords'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='seo_meta_keywords_fr',
            field=models.TextField(max_length=1000, unique=True, verbose_name='french meta keywords'),
        ),
    ]
