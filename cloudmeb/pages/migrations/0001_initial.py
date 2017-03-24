# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('seo_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='seos.Seo')),
                ('page_id', models.AutoField(primary_key=True, serialize=False)),
                ('page_name', models.CharField(verbose_name='page name', max_length=100, choices=[('HOME', 'Home'), ('CONFIGURATOR', 'Configurator'), ('PRICING', 'Pricing'), ('SOLUTIONS', 'Soultions'), ('BECOME_A_PARTNER', 'Become a partner'), ('CONTACT', 'Contact'), ('FAQ', 'Frequently asked questions'), ('TERMS_AND_CONDITIONS', 'Terms and conditions'), ('DYNAMIC_PARTNER', 'Dynamic partner'), ('DYNAMIC_SERVICE', 'Dynamic service'), ('DYNAMIC_PRODUCT', 'Dynamic product')])),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
            bases=('seos.seo',),
        ),
    ]
