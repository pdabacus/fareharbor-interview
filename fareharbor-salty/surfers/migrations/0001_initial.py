# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('shaping_since', models.DateField()),
                ('label', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True)),
                ('website_url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Surfboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_name', models.CharField(max_length=200)),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('description', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('shaper', models.ForeignKey(to='surfers.Shaper')),
            ],
        ),
        migrations.CreateModel(
            name='Surfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('skill', models.PositiveIntegerField()),
                ('bio', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='surfboard',
            name='surfer',
            field=models.ForeignKey(to='surfers.Surfer'),
        ),
    ]
