# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Solution',
            old_name='solution_short_name_fr',
            new_name='solution_tagline_fr'
        ),
        migrations.RenameField(
            model_name='Solution',
            old_name='solution_short_name_en',
            new_name='solution_tagline_en'
        ),
    ]
