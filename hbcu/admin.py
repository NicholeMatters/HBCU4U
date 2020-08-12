from django.contrib import admin
from .models import College, Major, HBCUgrads, Degree

# Register your models here.
admin.site.register(College)
admin.site.register(Major)
admin.site.register(HBCUgrads)
admin.site.register(Degree)