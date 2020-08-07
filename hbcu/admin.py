from django.contrib import admin
from .models import College

from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

# Register your models here.
admin.site.register(College)

class CityAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }