# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benefit',
            options={'verbose_name': 'benefit', 'verbose_name_plural': 'benefits', 'ordering': ['benefit_order']},
        ),
        migrations.AddField(
            model_name='benefit',
            name='benefit_order',
            field=models.IntegerField(verbose_name='order', blank=True, null=True),
        ),
    ]
