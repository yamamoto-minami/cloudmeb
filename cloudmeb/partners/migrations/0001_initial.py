# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('pages', '0001_initial'),
        ('products', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='pages.Page')),
                ('user_ptr', models.OneToOneField(auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('partner_id', models.AutoField(primary_key=True, serialize=False)),
                ('partner_description_en', models.TextField(verbose_name='English description')),
                ('partner_description_fr', models.TextField(verbose_name='French description')),
                ('partner_medium_description_en', models.TextField(verbose_name='English medium description')),
                ('partner_medium_description_fr', models.TextField(verbose_name='French medium description')),
                ('partner_short_description_en', models.TextField(verbose_name='English short description')),
                ('partner_short_description_fr', models.TextField(verbose_name='French short description')),
                ('partner_products', models.ManyToManyField(verbose_name='products', blank=True, to='products.Product')),
                ('partner_services', models.ManyToManyField(verbose_name='services', blank=True, to='services.Service')),
            ],
            options={
                'verbose_name': 'partner',
                'verbose_name_plural': 'partners',
            },
            bases=('users.user', 'pages.page'),
        ),
    ]
