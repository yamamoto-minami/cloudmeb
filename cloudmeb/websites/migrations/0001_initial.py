# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('site_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='sites.Site')),
                ('website_id', models.AutoField(primary_key=True, serialize=False)),
                ('smtp_user', models.EmailField(verbose_name='smtp user', max_length=254)),
                ('smtp_password', models.CharField(verbose_name='smtp password', max_length=500)),
                ('smtp_from_email', models.EmailField(verbose_name='smtp default email', max_length=254)),
                ('smtp_server', models.URLField(verbose_name='smtp server')),
                ('smtp_port', models.IntegerField(verbose_name='smtp port number')),
                ('smtp_tls', models.BooleanField(verbose_name='smtp use tls')),
                ('salesforce_id', models.CharField(verbose_name='salesforce id', max_length=255)),
                ('google_analytics_id', models.CharField(verbose_name='google analytics id', max_length=255)),
                ('google_addwords_id', models.CharField(verbose_name='google addwords id', max_length=255)),
                ('google_plus_id', models.CharField(verbose_name='google plus id', max_length=255)),
                ('twitter_id', models.CharField(verbose_name='twitter id', max_length=255)),
                ('facebook_id', models.CharField(verbose_name='facebook id', max_length=255)),
                ('linkedin_id', models.CharField(verbose_name='linkedin id', max_length=255)),
                ('shop_url', models.URLField(verbose_name='shop url')),
            ],
            options={
                'verbose_name': 'website',
                'verbose_name_plural': 'websites',
            },
            bases=('sites.site',),
        ),
    ]
