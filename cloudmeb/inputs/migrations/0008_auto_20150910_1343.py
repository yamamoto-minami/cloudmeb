# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0007_input_input_related_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='input_question_en',
            field=models.CharField(blank=True, verbose_name='english question', max_length=500),
        ),
        migrations.AddField(
            model_name='input',
            name='input_question_fr',
            field=models.CharField(blank=True, verbose_name='french question', max_length=500),
        ),
    ]
