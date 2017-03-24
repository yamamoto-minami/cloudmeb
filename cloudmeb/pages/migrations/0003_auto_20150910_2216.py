# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20150629_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_name',
            field=models.CharField(max_length=100, choices=[('HOME', 'Home'), ('CONFIGURATOR', 'Configurator'), ('PRICING', 'Pricing'), ('SOLUTIONS', 'Solutions'), ('BECOME_A_PARTNER', 'Become a partner'), ('CONTACT', 'Contact'), ('FAQ', 'Frequently asked questions'), ('TERMS_AND_CONDITIONS', 'Terms and conditions'), ('PRIVACY_POLICY', 'Privacy policy'), ('DYNAMIC_PARTNER', 'Dynamic partner'), ('DYNAMIC_SERVICE', 'Dynamic service'), ('DYNAMIC_PRODUCT', 'Dynamic product')], verbose_name='page name'),
        ),
    ]
