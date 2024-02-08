from django.contrib import admin
from .models import Cleanse, CleanseEntry, Restriction

# Register your models here.
admin.site.register(Cleanse)

admin.site.register(CleanseEntry)

admin.site.register(Restriction)
