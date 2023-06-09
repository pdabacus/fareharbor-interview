# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-05-25 11:21
from __future__ import unicode_literals

from django.db import migrations


def populate_many_to_many_surfboards_shapers(apps, schema_editor):
    """
    Creating Surfboards.shapers many-to-many relation to allow for a
    surfboard to have multiple collaborative creators

    Once migration complete, then the Surfboard.shaper many-to-one field will
    be removed and replaced by the use of the shapers field
    """
    Surfboard = apps.get_model("surfers", "Surfboard")
    for surfboard in Surfboard.objects.all():
        surfboard.shapers.add(surfboard.shaper)


class Migration(migrations.Migration):

    dependencies = [
        ('surfers', '0002_surfboard_shapers'),
    ]

    operations = [
        migrations.RunPython(populate_many_to_many_surfboards_shapers),
    ]
