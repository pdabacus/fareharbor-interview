from django.shortcuts import (
    render, get_object_or_404,
)
from django.db.models import Max

from surfers.models import (
    Surfer, Shaper, Surfboard
)


def index(request):
    return render(request, 'index.html', {
        'new_surfboards': Surfboard.objects.order_by('-created_at')[:3],
        'updated_shapers': Shaper.objects.annotate(recent=Max('surfboard__created_at')).order_by('-recent')[:2]
    })


def surfers(request):
    surfers = Surfer.objects.all()
    return render(request, 'surfers.html', {
        'surfers': surfers,
    })


def surfer(request, surfer_pk):
    surfer = get_object_or_404(Surfer, pk=surfer_pk)
    return render(request, 'surfer.html', {
        'surfer': surfer,
    })


def shapers(request):
    shapers = Shaper.objects.all()
    return render(request, 'shapers.html', {
        'shapers': shapers,
    })


def shaper(request, shaper_pk):
    shaper = get_object_or_404(Shaper, pk=shaper_pk)
    return render(request, 'shaper.html', {
        'shaper': shaper,
    })


def surfboards(request):
    surfboards = Surfboard.objects.all()
    return render(request, 'surfboards.html', {
        'surfboards': surfboards,
    })


def surfboard(request, surfboard_pk):
    surfboard = get_object_or_404(Surfboard, pk=surfboard_pk)
    return render(request, 'surfboard.html', {
        'surfboard': surfboard,
    })
