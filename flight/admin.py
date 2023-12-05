from django.contrib import admin
from . import models


@admin.register(models.Airline)
class AirlineModelAdmin(admin.ModelAdmin):
    pass
