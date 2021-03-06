# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Become_partner_txt',
            fields=[
                ('become_partner_txt_id', models.AutoField(primary_key=True, serialize=False)),
                ('become_partner_txt_name', models.CharField(verbose_name='page name', choices=[('WHY_CLOUDMEB', 'Why Cloudmeb'), ('PLUG_IN_YOUR_BUSINESS', 'Plug-in your business'), ('SOLUTIONS', 'Solutions'), ('BECOME_A_PARTNER', 'Become a partner'), ('CONTACT_US', 'Contact us'), ('FREQUENTLY_ASKED_QUESTIONS', 'Frequently asked questions')], max_length=100)),
                ('become_partner_txt_header_title_en', models.CharField(verbose_name='english banner header title', unique=True, max_length=300)),
                ('become_partner_txt_header_title_fr', models.CharField(verbose_name='french banner header title', unique=True, max_length=300)),
                ('become_partner_txt_header_subtitle_en', models.CharField(verbose_name='english banner header sub title', unique=True, max_length=300)),
                ('become_partner_txt_header_subtitle_fr', models.CharField(verbose_name='french banner header sub title', unique=True, max_length=300)),
                ('become_partner_txt_content_title_en', models.CharField(verbose_name='english content title', unique=True, max_length=300)),
                ('become_partner_txt_content_title_fr', models.CharField(verbose_name='french content title', unique=True, max_length=300)),
                ('become_partner_txt_content_level1_title_en', models.CharField(verbose_name='english content level1 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level1_title_fr', models.CharField(verbose_name='french content level1 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level1_text_en', models.TextField(verbose_name='english content level1 text')),
                ('become_partner_txt_content_level1_text_fr', models.TextField(verbose_name='french content level1 text')),
                ('become_partner_txt_content_level11_title_en', models.CharField(verbose_name='english content level11 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level11_title_fr', models.CharField(verbose_name='french content level11 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level11_text_en', models.TextField(verbose_name='english content level11 text')),
                ('become_partner_txt_content_level11_text_fr', models.TextField(verbose_name='french content level11 text')),
                ('become_partner_txt_content_level12_title_en', models.CharField(verbose_name='english content level12 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level12_title_fr', models.CharField(verbose_name='french content level12 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level12_text_en', models.TextField(verbose_name='english content level12 text')),
                ('become_partner_txt_content_level12_text_fr', models.TextField(verbose_name='french content level12 text')),
                ('become_partner_txt_content_level13_title_en', models.CharField(verbose_name='english content level13 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level13_title_fr', models.CharField(verbose_name='french content level13 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level13_text_en', models.TextField(verbose_name='english content level13 text')),
                ('become_partner_txt_content_level13_text_fr', models.TextField(verbose_name='french content level13 text')),
                ('become_partner_txt_content_level2_title_en', models.CharField(verbose_name='english content level2 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level2_title_fr', models.CharField(verbose_name='french content level2 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level2_text_en', models.TextField(verbose_name='english content level2 text')),
                ('become_partner_txt_content_level2_text_fr', models.TextField(verbose_name='french content level2 text')),
                ('become_partner_txt_content_level21_title_en', models.CharField(verbose_name='english content level21 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level21_title_fr', models.CharField(verbose_name='french content level21 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level21_text_en', models.TextField(verbose_name='english content level21 text')),
                ('become_partner_txt_content_level21_text_fr', models.TextField(verbose_name='french content level21 text')),
                ('become_partner_txt_content_level22_title_en', models.CharField(verbose_name='english content level22 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level22_title_fr', models.CharField(verbose_name='french content level22 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level22_text_en', models.TextField(verbose_name='english content level22 text')),
                ('become_partner_txt_content_level22_text_fr', models.TextField(verbose_name='french content level22 text')),
                ('become_partner_txt_content_level23_title_en', models.CharField(verbose_name='english content level23 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level23_title_fr', models.CharField(verbose_name='french content level23 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level23_text_en', models.TextField(verbose_name='english content level23 text')),
                ('become_partner_txt_content_level23_text_fr', models.TextField(verbose_name='french content level23 text')),
                ('become_partner_txt_content_level3_title_en', models.CharField(verbose_name='english content level3 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level3_title_fr', models.CharField(verbose_name='french content level3 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level3_text_en', models.TextField(verbose_name='english content level3 text')),
                ('become_partner_txt_content_level3_text_fr', models.TextField(verbose_name='french content level3 text')),
                ('become_partner_txt_content_level31_title_en', models.CharField(verbose_name='english content level31 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level31_title_fr', models.CharField(verbose_name='french content level31 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level31_text_en', models.TextField(verbose_name='english content level31 text')),
                ('become_partner_txt_content_level31_text_fr', models.TextField(verbose_name='french content level31 text')),
                ('become_partner_txt_content_level32_title_en', models.CharField(verbose_name='english content level32 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level32_title_fr', models.CharField(verbose_name='french content level32 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level32_text_en', models.TextField(verbose_name='english content level32 text')),
                ('become_partner_txt_content_level32_text_fr', models.TextField(verbose_name='french content level32 text')),
                ('become_partner_txt_content_level33_title_en', models.CharField(verbose_name='english content level33 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level33_title_fr', models.CharField(verbose_name='french content level33 title', unique=True, max_length=300)),
                ('become_partner_txt_content_level33_text_en', models.TextField(verbose_name='english content level33 text')),
                ('become_partner_txt_content_level33_text_fr', models.TextField(verbose_name='french content level33 text')),
                ('become_partner_txt_step_title_en', models.CharField(verbose_name='english step title', unique=True, max_length=300)),
                ('become_partner_txt_step_title_fr', models.CharField(verbose_name='french step title', unique=True, max_length=300)),
                ('become_partner_txt_step_subtitle1_en', models.CharField(verbose_name='english step subtitle1', unique=True, max_length=300)),
                ('become_partner_txt_step_subtitle1_fr', models.CharField(verbose_name='french step subtitle1', unique=True, max_length=300)),
                ('become_partner_txt_step_subtext1_en', models.TextField(verbose_name='english step subtext1 text')),
                ('become_partner_txt_step_subtext1_fr', models.TextField(verbose_name='french step subtext1 text')),
                ('become_partner_txt_step_subtitle2_en', models.CharField(verbose_name='english step subtitle2', unique=True, max_length=300)),
                ('become_partner_txt_step_subtitle2_fr', models.CharField(verbose_name='french step subtitle2', unique=True, max_length=300)),
                ('become_partner_txt_step_subtext2_en', models.TextField(verbose_name='english step subtext2 text')),
                ('become_partner_txt_step_subtext2_fr', models.TextField(verbose_name='french step subtext2 text')),
                ('become_partner_txt_step_subtitle3_en', models.CharField(verbose_name='english step subtitle3', unique=True, max_length=300)),
                ('become_partner_txt_step_subtitle3_fr', models.CharField(verbose_name='french step subtitle3', unique=True, max_length=300)),
                ('become_partner_txt_step_subtext3_en', models.TextField(verbose_name='english step subtext3 text')),
                ('become_partner_txt_step_subtext3_fr', models.TextField(verbose_name='french step subtext3 text')),
                ('become_partner_txt_say_title_en', models.CharField(verbose_name='english partner say title', unique=True, max_length=300)),
                ('become_partner_txt_say_title_fr', models.CharField(verbose_name='french partner say title', unique=True, max_length=300)),
                ('become_partner_txt_form_title_en', models.CharField(verbose_name='english step form title', unique=True, max_length=300)),
                ('become_partner_txt_form_title_fr', models.CharField(verbose_name='french step form title', unique=True, max_length=300)),
                ('become_partner_txt_form_text_en', models.TextField(verbose_name='english step form text')),
                ('become_partner_txt_form_text_fr', models.TextField(verbose_name='french step form text')),
            ],
            options={
                'verbose_name': 'become_partner_txt',
                'verbose_name_plural': 'become_partner_txts',
            },
        ),
    ]
