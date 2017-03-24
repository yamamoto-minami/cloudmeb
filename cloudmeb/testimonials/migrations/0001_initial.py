# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0005_auto_20150906_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('testimonial_id', models.AutoField(serialize=False, primary_key=True)),
                ('testimonial_type', models.CharField(choices=[('CLIENT', 'Client'), ('PARTNER', 'Partner')], max_length=100, verbose_name='type')),
                ('testimonial_full_name', models.CharField(max_length=200, verbose_name='full name')),
                ('testimonial_company_name_en', models.CharField(max_length=200, verbose_name='english company name')),
                ('testimonial_company_name_fr', models.CharField(max_length=200, verbose_name='french company name')),
                ('testimonial_position_en', models.CharField(max_length=200, verbose_name='english company position')),
                ('testimonial_position_fr', models.CharField(max_length=200, verbose_name='french company position')),
                ('testimonial_body_en', models.TextField(verbose_name='english body')),
                ('testimonial_body_fr', models.TextField(verbose_name='french body')),
                ('testimonial_mugshot', models.ImageField(default='placeholders/mugshot.png', upload_to='testimonials/', verbose_name='mugshot')),
                ('testimonial_solutions', models.ManyToManyField(to='solutions.Solution', verbose_name='solutions')),
            ],
            options={
                'verbose_name_plural': 'testimonials',
                'verbose_name': 'testimonial',
            },
        ),
    ]
