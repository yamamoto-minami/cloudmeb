# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shared_txt',
            fields=[
                ('shared_txt_id', models.AutoField(serialize=False, primary_key=True)),
                ('shared_txt_name', models.CharField(verbose_name='shared name', max_length=300, unique=True)),
                ('shared_txt_name_en', models.CharField(verbose_name='shared name english', max_length=300, unique=True)),
                ('shared_txt_name_fr', models.CharField(verbose_name='shared name french', max_length=300, unique=True)),
            ],
            options={
                'verbose_name_plural': 'shared_txts',
                'verbose_name': 'shared_txt',
            },
        ),
    ]
