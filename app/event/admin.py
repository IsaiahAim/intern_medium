from django.contrib import admin
from .models import Event, Categorie

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Event)