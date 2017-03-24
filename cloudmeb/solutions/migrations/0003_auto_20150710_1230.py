# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_auto_20150710_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution_tagline_en',
            field=models.CharField(max_length=100, verbose_name='english tagline', unique=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='solution_tagline_fr',
            field=models.CharField(max_length=100, verbose_name='french tagline', unique=True),
        ),
    ]
