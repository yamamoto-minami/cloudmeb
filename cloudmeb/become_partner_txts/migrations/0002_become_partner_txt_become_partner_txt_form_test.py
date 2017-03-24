# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('become_partner_txts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='become_partner_txt',
            name='become_partner_txt_form_test',
            field=models.TextField(default='test', verbose_name='test'),
        ),
    ]
