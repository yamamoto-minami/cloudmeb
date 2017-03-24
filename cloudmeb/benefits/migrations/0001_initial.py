# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('benefit_id', models.AutoField(primary_key=True, serialize=False)),
                ('benefit_name_en', models.CharField(verbose_name='english name', max_length=200, unique=True)),
                ('benefit_name_fr', models.CharField(verbose_name='french name', max_length=200, unique=True)),
                ('benefit_short_name_en', models.CharField(verbose_name='english short name', max_length=100, unique=True)),
                ('benefit_short_name_fr', models.CharField(verbose_name='french short name', max_length=100, unique=True)),
                ('benefit_description_en', models.TextField(verbose_name='english description', max_length=1000, unique=True)),
                ('benefit_description_fr', models.TextField(verbose_name='french description', max_length=1000, unique=True)),
                ('benefit_medium_description_en', models.TextField(verbose_name='english medium description', max_length=500, unique=True)),
                ('benefit_medium_description_fr', models.TextField(verbose_name='french medium description', max_length=500, unique=True)),
                ('benefit_short_description_en', models.TextField(verbose_name='english short description', max_length=250, unique=True)),
                ('benefit_short_description_fr', models.TextField(verbose_name='french short description', max_length=250, unique=True)),
                ('benefit_image_en', models.ImageField(verbose_name='english image', default='placeholders/300x300.gif', upload_to='benefits/')),
                ('benefit_image_fr', models.ImageField(verbose_name='french image', default='placeholders/300x300.gif', upload_to='benefits/')),
            ],
            options={
                'verbose_name': 'benefit',
                'verbose_name_plural': 'benefits',
            },
        ),
    ]
