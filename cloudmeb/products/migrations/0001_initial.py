# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
        ('pages', '0001_initial'),
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='pages.Page')),
                ('price_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='prices.Price')),
                ('solution_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='solutions.Solution')),
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('site_url', models.URLField(verbose_name='site url', blank=True)),
                ('product_featured', models.BooleanField(verbose_name='featured')),
                ('product_order', models.IntegerField(verbose_name='order', unique=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
            bases=('solutions.solution', 'prices.price', 'pages.page'),
        ),
    ]
