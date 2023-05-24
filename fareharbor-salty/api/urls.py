from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'surfers', views.SurfersViewSet)
router.register(r'shapers', views.ShapersViewSet)
router.register(r'surfboards', views.SurfboardsViewSet)

urlpatterns = [
    url(r"^$", views.index),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])

urlpatterns += [
    url("", include(router.urls))
]