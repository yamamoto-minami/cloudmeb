# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solution_page_txt',
            fields=[
                ('solution_page_txt_id', models.AutoField(serialize=False, primary_key=True)),
                ('solution_page_txt_name', models.CharField(choices=[('WHY_CLOUDMEB', 'Why Cloudmeb'), ('PLUG_IN_YOUR_BUSINESS', 'Plug-in your business'), ('SOLUTIONS', 'Solutions'), ('BECOME_A_PARTNER', 'Become a partner'), ('CONTACT_US', 'Contact us'), ('FREQUENTLY_ASKED_QUESTIONS', 'Frequently asked questions')], verbose_name='page name', max_length=100)),
                ('solution_page_txt_header_title_en', models.CharField(unique=True, verbose_name='english banner header title', max_length=300)),
                ('solution_page_txt_header_title_fr', models.CharField(unique=True, verbose_name='french banner header title', max_length=300)),
                ('solution_page_txt_header_subtitle_en', models.CharField(unique=True, verbose_name='english banner header sub title', max_length=300)),
                ('solution_page_txt_header_subtitle_fr', models.CharField(unique=True, verbose_name='french banner header sub title', max_length=300)),
                ('solution_page_txt_product_title_en', models.CharField(unique=True, verbose_name='english product title', max_length=300)),
                ('solution_page_txt_product_title_fr', models.CharField(unique=True, verbose_name='french product title', max_length=300)),
                ('solution_page_txt_service_title_en', models.CharField(unique=True, verbose_name='english service title', max_length=300)),
                ('solution_page_txt_service_title_fr', models.CharField(unique=True, verbose_name='french service title', max_length=300)),
                ('solution_page_txt_cta_text_en', models.TextField(verbose_name='english cta text')),
                ('solution_page_txt_cta_text_fr', models.TextField(verbose_name='french cta text')),
            ],
            options={
                'verbose_name': 'solution_page_txt',
                'verbose_name_plural': 'solution_page_txts',
            },
        ),
    ]
