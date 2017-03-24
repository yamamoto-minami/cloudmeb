# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0003_auto_20150710_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution_categories',
            field=models.ManyToManyField(related_name='solutions', to='categories.Category', verbose_name='categories'),
        ),
    ]
