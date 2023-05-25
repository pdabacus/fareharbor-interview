# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-05-25 16:24
from __future__ import unicode_literals

from django.db import migrations

def populate_many_to_one_surfboard_models(apps, schema_editor):
    """
    Creating Surfboard.surfboard_model many-to-one relation to allow for a
    SurfboardModel to have multiple surfboards attached to it like unique grouping
    """
    Surfboard = apps.get_model("surfers", "Shaper")
    Surfboard = apps.get_model("surfers", "Surfboard")
    SurfboardModel = apps.get_model("surfers", "SurfboardModel")

    collaboration_possibilities = dict() # tuple[Shaper.id] -> list[Surfboard]
    for surfboard in Surfboard.objects.all():
        collaborators = tuple(sorted(set([shaper.id for shaper in surfboard.shapers.all()])))
        if collaborators in collaboration_possibilities:
            collaboration_possibilities[collaborators].append(surfboard)
        else:
            collaboration_possibilities[collaboration_possibilities] = [surfboard]
    for collaborators, surfboards in collaboration_possibilities.items():
        collaborator_names = [Shaper.]
        model_name = 



class Migration(migrations.Migration):

    dependencies = [
        ('surfers', '0007_auto_20230525_1609'),
    ]

    operations = [
        migrations.RunPython(populate_many_to_many_surfboards_shapers),
    ]
