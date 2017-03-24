# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('experience_id', models.AutoField(primary_key=True, serialize=False)),
                ('experience_class_name', models.CharField(verbose_name='class name', max_length=200)),
                ('experience_menu_tab_name_en', models.CharField(verbose_name='english menu tab name', max_length=200)),
                ('experience_menu_tab_name_fr', models.CharField(verbose_name='french menu tab name', max_length=200)),
                ('experience_body_top_en', models.TextField(verbose_name='english body top')),
                ('experience_body_top_fr', models.TextField(verbose_name='french body top')),
                ('experience_body_bottom_en', models.TextField(verbose_name='english body bottom')),
                ('experience_body_bottom_fr', models.TextField(verbose_name='french body bottom')),
                ('experience_order', models.IntegerField(blank=True, null=True, verbose_name='order')),
                ('experience_background', models.ImageField(default='placeholders/1600x500.gif', verbose_name='background', upload_to='experiences/')),
            ],
            options={
                'verbose_name': 'experience',
                'verbose_name_plural': 'experiences',
            },
        ),
    ]
