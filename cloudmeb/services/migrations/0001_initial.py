# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='pages.Page')),
                ('solution_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='solutions.Solution')),
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_order', models.IntegerField(verbose_name='order', unique=True)),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
            bases=('solutions.solution', 'pages.page'),
        ),
    ]
