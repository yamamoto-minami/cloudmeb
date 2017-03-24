# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0002_input_input_default_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='input_display',
            field=models.BooleanField(verbose_name='display', default=False),
        ),
    ]

    # def forwards(self, orm):
    #     # Disable foreign key checks during fixture loading
    #     from django.db import connections, DEFAULT_DB_ALIAS
    #     connection = connections[DEFAULT_DB_ALIAS]
    #     if 'mysql' in connection.settings_dict['ENGINE']:
    #         cursor = connection.cursor()
    #         cursor.execute('SET foreign_key_checks = 0')

    #     # Load fixture
    #     from django.core.management import call_command
    #     call_command('loaddata', 'initial_data.json', verbosity=0)

    #     # Enable foreign key checks after fixture loading
    #     if 'mysql' in connection.settings_dict['ENGINE']:
    #         cursor = connection.cursor()
    #         cursor.execute('SET foreign_key_checks = 1')
    #     connection.close()