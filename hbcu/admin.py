from django.contrib import admin
from .models import College, Major, HBCUgrads, State, Degree

# Register your models here.
admin.site.register(College)
admin.site.register(Major)
admin.site.register(HBCUgrads)
admin.site.register(State)
admin.site.register(Degree)