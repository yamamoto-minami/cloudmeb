# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('input_id', models.AutoField(primary_key=True, serialize=False)),
                ('input_type', models.CharField(verbose_name='type', max_length=100, choices=[('OPTIONS', 'Options'), ('MULTI_OPTIONS', 'Multi options'), ('RADIO', 'Radio'), ('CHECKBOX', 'Checkbox'), ('NUMBER', 'Number')])),
                ('input_name', models.CharField(verbose_name='name', max_length=50)),
                ('input_label_en', models.CharField(verbose_name='english label', max_length=200)),
                ('input_label_fr', models.CharField(verbose_name='french label', max_length=200)),
                ('input_placeholder_en', models.CharField(verbose_name='english placeholder', blank=True, max_length=200)),
                ('input_placeholder_fr', models.CharField(verbose_name='french placeholder', blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'input',
                'verbose_name_plural': 'inputs',
            },
        ),
    ]
