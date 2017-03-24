# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Why_cloudmeb_txt',
            fields=[
                ('why_cloudmeb_txt_id', models.AutoField(primary_key=True, serialize=False)),
                ('why_cloudmeb_txt_name', models.CharField(choices=[('WHY_CLOUDMEB', 'Why Cloudmeb'), ('PLUG_IN_YOUR_BUSINESS', 'Plug-in your business'), ('SOLUTIONS', 'Solutions'), ('BECOME_A_PARTNER', 'Become a partner'), ('CONTACT_US', 'Contact us'), ('FREQUENTLY_ASKED_QUESTIONS', 'Frequently asked questions')], max_length=100, verbose_name='page name')),
                ('why_cloudmeb_txt_header_title_en', models.CharField(verbose_name='english banner header title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_header_title_fr', models.CharField(verbose_name='french banner header title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_header_subtitle_en', models.CharField(verbose_name='english banner header sub title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_header_subtitle_fr', models.CharField(verbose_name='french banner header sub title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_introduce_title_en', models.CharField(verbose_name='english introduce title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_introduce_title_fr', models.CharField(verbose_name='french introduce title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_introduce_text_en', models.TextField(verbose_name='english introduce text')),
                ('why_cloudmeb_txt_introduce_text_fr', models.TextField(verbose_name='french introduce text')),
                ('why_cloudmeb_txt_why_introduce_title_en', models.CharField(verbose_name='english why introduce title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_why_introduce_title_fr', models.CharField(verbose_name='french why introduce title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_why_introduce_text_en', models.TextField(verbose_name='english why introduce text')),
                ('why_cloudmeb_txt_why_introduce_text_fr', models.TextField(verbose_name='french why introduce text')),
                ('why_cloudmeb_txt_whytab_title_en', models.CharField(verbose_name='english whytab title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_whytab_title_fr', models.CharField(verbose_name='french whytab title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_whytab_subtitle_en', models.CharField(verbose_name='english whytab sub title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_whytab_subtitle_fr', models.CharField(verbose_name='french whytab sub title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_cta_text_en', models.TextField(verbose_name='english cta text')),
                ('why_cloudmeb_txt_cta_text_fr', models.TextField(verbose_name='french cta text')),
                ('why_cloudmeb_txt_logo_slider_title_en', models.CharField(verbose_name='english logo slider title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_logo_slider_title_fr', models.CharField(verbose_name='french logo slider title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_experience_title_en', models.CharField(verbose_name='english experience title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_experience_title_fr', models.CharField(verbose_name='french experience title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_testimonial_title_en', models.CharField(verbose_name='english testimonial title', max_length=300, unique=True)),
                ('why_cloudmeb_txt_testimonial_title_fr', models.CharField(verbose_name='french testimonial title', max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'why_cloudmeb_txt',
                'verbose_name_plural': 'why_cloudmeb_txts',
            },
        ),
    ]
