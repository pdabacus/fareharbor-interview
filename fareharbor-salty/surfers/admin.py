from django.contrib import admin

from .models import Surfer, Shaper, SurfboardModel, Surfboard


admin.site.register(Surfer)
admin.site.register(Shaper)
admin.site.register(SurfboardModel)
admin.site.register(Surfboard)
