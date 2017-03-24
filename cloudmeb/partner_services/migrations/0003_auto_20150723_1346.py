# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner_services', '0002_auto_20150626_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerservice',
            name='partner_service_service',
            field=models.ForeignKey(verbose_name='service', to='services.Service', related_name='partner_services'),
        ),
    ]
