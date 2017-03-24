# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('partner_services', '0001_initial'),
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnerservice',
            name='partner_service_partner',
            field=models.ForeignKey(verbose_name='partner', to='partners.Partner'),
        ),
        migrations.AddField(
            model_name='partnerservice',
            name='partner_service_service',
            field=models.ForeignKey(verbose_name='service', to='services.Service'),
        ),
    ]
