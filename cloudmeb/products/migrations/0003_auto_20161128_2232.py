# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150626_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_order',
            field=models.IntegerField(unique=True, verbose_name='order', default='0'),
        ),
    ]
