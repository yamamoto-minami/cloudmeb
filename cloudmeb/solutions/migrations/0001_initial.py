# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('values', '0001_initial'),
        ('benefits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('solution_id', models.AutoField(primary_key=True, serialize=False)),
                ('solution_name_en', models.CharField(verbose_name='english name', max_length=200, unique=True)),
                ('solution_name_fr', models.CharField(verbose_name='french name', max_length=200, unique=True)),
                ('solution_short_name_en', models.CharField(verbose_name='english short name', max_length=100, unique=True)),
                ('solution_short_name_fr', models.CharField(verbose_name='french short name', max_length=100, unique=True)),
                ('solution_description_en', models.TextField(verbose_name='english description')),
                ('solution_description_fr', models.TextField(verbose_name='french description')),
                ('solution_medium_description_en', models.TextField(verbose_name='english medium description')),
                ('solution_medium_description_fr', models.TextField(verbose_name='french medium description')),
                ('solution_short_description_en', models.TextField(verbose_name='english short description')),
                ('solution_short_description_fr', models.TextField(verbose_name='french short description')),
                ('solution_image_en', models.ImageField(verbose_name='english image', default='placeholders/300x300.gif', upload_to='solutions/')),
                ('solution_image_fr', models.ImageField(verbose_name='french image', default='placeholders/300x300.gif', upload_to='solutions/')),
                ('solution_banner_en', models.ImageField(verbose_name='english banner', default='placeholders/1600x500.gif', upload_to='solutions/')),
                ('solution_banner_fr', models.ImageField(verbose_name='french banner', default='placeholders/1600x500.gif', upload_to='solutions/')),
                ('solution_icon_en', models.ImageField(verbose_name='english icon', default='placeholders/300x300.gif', upload_to='solutions/')),
                ('solution_icon_fr', models.ImageField(verbose_name='french icon', default='placeholders/300x300.gif', upload_to='solutions/')),
                ('solution_logo_en', models.ImageField(verbose_name='english logo', default='placeholders/100x100.gif', upload_to='solutions/')),
                ('solution_logo_fr', models.ImageField(verbose_name='french logo', default='placeholders/100x100.gif', upload_to='solutions/')),
                ('solution_slug_en', models.SlugField(verbose_name='english slug', blank=True, max_length=100, unique=True)),
                ('solution_slug_fr', models.SlugField(verbose_name='french slug', blank=True, max_length=100, unique=True)),
                ('solution_benefits', models.ManyToManyField(verbose_name='benefils', to='benefits.Benefit')),
                ('solution_categories', models.ManyToManyField(verbose_name='categories', to='categories.Category')),
                ('solution_values', models.ManyToManyField(verbose_name='values', to='values.Value')),
            ],
            options={
                'verbose_name': 'solution',
                'verbose_name_plural': 'solutions',
            },
        ),
    ]
