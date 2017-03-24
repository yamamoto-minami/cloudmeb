# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0005_auto_20150906_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution_benefits',
            field=models.ManyToManyField(verbose_name='benefits', to='benefits.Benefit'),
        ),
    ]
