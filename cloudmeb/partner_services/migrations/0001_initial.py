# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerService',
            fields=[
                ('price_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='prices.Price')),
                ('partner_service_id', models.AutoField(primary_key=True, serialize=False)),
                ('partner_service_featured', models.BooleanField(verbose_name='featured')),
            ],
            options={
                'verbose_name': 'partner service',
                'verbose_name_plural': 'partner services',
            },
            bases=('prices.price',),
        ),
    ]
