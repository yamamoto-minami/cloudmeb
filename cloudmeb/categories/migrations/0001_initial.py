# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name_en', models.CharField(verbose_name='english name', max_length=200, unique=True)),
                ('category_name_fr', models.CharField(verbose_name='french name', max_length=200, unique=True)),
                ('category_short_name_en', models.CharField(verbose_name='english short name', max_length=100, unique=True)),
                ('category_short_name_fr', models.CharField(verbose_name='french short name', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
