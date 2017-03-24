# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20161128_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_order',
            field=models.IntegerField(verbose_name='order', unique=True),
        ),
    ]
