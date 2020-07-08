from django.contrib import admin
from .models import Zapatilla

# Register your models here.
admin.site.site_header = 'Zapandilla Admin'

admin.site.register(Zapatilla)

class Zapatilla(admin.ModelAdmin):
    list_display = ('description', 'price')