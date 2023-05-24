from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from surfers.models import (
    Surfer, Shaper, Surfboard
)

from surfers.serializers import (
    SurferSerializer, ShaperSerializer, SurfboardSerializer
)


@api_view(["GET", "POST"])
def index(request, format=None):
    if request.method == "GET":
        return Response({"version": "1.0", "method": "get"})
    elif request.method == "POST":
        return Response({"version": "1.0", "method": "post"})


class SurfersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Surfer.objects.all()
    serializer_class = SurferSerializer


class ShapersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Shaper.objects.all()
    serializer_class = ShaperSerializer


class SurfboardsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Surfboard.objects.all()
    serializer_class = SurfboardSerializer
