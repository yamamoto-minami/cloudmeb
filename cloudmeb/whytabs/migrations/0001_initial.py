# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Whytab',
            fields=[
                ('whytab_id', models.AutoField(serialize=False, primary_key=True)),
                ('whytab_class_name', models.CharField(max_length=200, verbose_name='class name', unique=True)),
                ('whytab_menu_name_en', models.CharField(max_length=200, verbose_name='english menu name', unique=True)),
                ('whytab_menu_name_fr', models.CharField(max_length=200, verbose_name='french menu name', unique=True)),
                ('whytab_left_title_en', models.CharField(max_length=200, verbose_name='english left title name', unique=True)),
                ('whytab_left_title_fr', models.CharField(max_length=200, verbose_name='french left title name', unique=True)),
                ('whytab_left_content_en', models.TextField(max_length=1000, verbose_name='english left content', unique=True)),
                ('whytab_left_content_fr', models.TextField(max_length=1000, verbose_name='french left content', unique=True)),
                ('whytab_left_icon', models.ImageField(upload_to='whytabs/', default='placeholders/50x50.gif', verbose_name='leftside icon')),
                ('whytab_right_title_en', models.CharField(max_length=200, verbose_name='english right title name', unique=True)),
                ('whytab_right_title_fr', models.CharField(max_length=200, verbose_name='french right title name', unique=True)),
                ('whytab_right_content_en', models.TextField(max_length=1000, verbose_name='english right content', unique=True)),
                ('whytab_right_content_fr', models.TextField(max_length=1000, verbose_name='french right content', unique=True)),
                ('whytab_right_slug_en', models.CharField(max_length=200, verbose_name='english right slug name', unique=True)),
                ('whytab_right_slug_fr', models.CharField(max_length=200, verbose_name='french right slug name', unique=True)),
                ('whytab_right_icon', models.ImageField(upload_to='whytabs/', default='placeholders/50x50.gif', verbose_name='rightside icon')),
                ('whytab_order', models.IntegerField(null=True, blank=True, verbose_name='order')),
            ],
            options={
                'ordering': ['whytab_order'],
                'verbose_name_plural': 'whytabs',
                'verbose_name': 'whytab',
            },
        ),
    ]
