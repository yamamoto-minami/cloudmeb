# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing_txt',
            fields=[
                ('Pricing_txt_id', models.AutoField(primary_key=True, serialize=False)),
                ('Pricing_txt_name', models.CharField(verbose_name='page name', max_length=100, choices=[('WHY_CLOUDMEB', 'Why Cloudmeb'), ('PLUG_IN_YOUR_BUSINESS', 'Plug-in your business'), ('SOLUTIONS', 'Solutions'), ('BECOME_A_PARTNER', 'Become a partner'), ('CONTACT_US', 'Contact us'), ('FREQUENTLY_ASKED_QUESTIONS', 'Frequently asked questions')])),
                ('Pricing_txt_header_title_en', models.CharField(unique=True, verbose_name='english banner header title', max_length=300)),
                ('Pricing_txt_header_title_fr', models.CharField(unique=True, verbose_name='french banner header title', max_length=300)),
                ('Pricing_txt_header_subtitle_en', models.CharField(unique=True, verbose_name='english banner header sub title', max_length=300)),
                ('Pricing_txt_header_subtitle_fr', models.CharField(unique=True, verbose_name='french banner header sub title', max_length=300)),
                ('Pricing_txt_product_title_en', models.CharField(unique=True, verbose_name='english product title', max_length=300)),
                ('Pricing_txt_product_title_fr', models.CharField(unique=True, verbose_name='french product title', max_length=300)),
                ('Pricing_txt_service_title_en', models.CharField(unique=True, verbose_name='english service title', max_length=300)),
                ('Pricing_txt_service_title_fr', models.CharField(unique=True, verbose_name='french service title', max_length=300)),
                ('Pricing_txt_showbtn_product_en', models.TextField(verbose_name='english Show more product button text')),
                ('Pricing_txt_showbtn_product_fr', models.TextField(verbose_name='french Show more product button text')),
                ('Pricing_txt_showbtn_service_en', models.TextField(verbose_name='english Show more service button text')),
                ('Pricing_txt_showbtn_service_fr', models.TextField(verbose_name='french Show more service button text')),
                ('Pricing_txt_monthly_title_en', models.TextField(verbose_name='english monthly title')),
                ('Pricing_txt_monthly_title_fr', models.TextField(verbose_name='french monthly title')),
                ('Pricing_txt_monthly_subtitle_en', models.TextField(verbose_name='english monthly subtitle')),
                ('Pricing_txt_monthly_subtitle_fr', models.TextField(verbose_name='french monthly subtitle')),
                ('Pricing_txt_monthly_btn_en', models.CharField(unique=True, verbose_name='english monthly button', max_length=300)),
                ('Pricing_txt_monthly_btn_fr', models.CharField(unique=True, verbose_name='french monthly button', max_length=300)),
                ('Pricing_txt_onetime_title_en', models.TextField(verbose_name='english onetime title')),
                ('Pricing_txt_onetime_title_fr', models.TextField(verbose_name='french onetime title')),
                ('Pricing_txt_onetime_subtitle_en', models.TextField(verbose_name='english onetime subtitle')),
                ('Pricing_txt_onetime_subtitle_fr', models.TextField(verbose_name='french onetime subtitle')),
                ('Pricing_txt_onetime_btn_en', models.CharField(unique=True, verbose_name='english onetime button', max_length=300)),
                ('Pricing_txt_onetime_btn_fr', models.CharField(unique=True, verbose_name='french onetime button', max_length=300)),
            ],
            options={
                'verbose_name': 'pricing_txt',
                'verbose_name_plural': 'pricing_txts',
            },
        ),
    ]
