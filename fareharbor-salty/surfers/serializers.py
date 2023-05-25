from rest_framework import serializers
from surfers.models import Surfer, Shaper, Surfboard

class SurferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Surfer
        fields = ["id", "name", "skill", "bio", "image_url"]


class ShaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shaper
        fields = ["id", "name", "shaping_since", "label", "bio", "website_url"]


class SurfboardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Surfboard
        fields = ["id", "model_name", "length", "width", "description", "image_url", "created_at", "shapers", "surfer"]