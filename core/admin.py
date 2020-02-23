from django.contrib import admin
from core.models import Evento

# Registro seu modelo aqui

class EventoAdmin(admin.ModelAdmin):

    list_display = ('titulo','data_evento','data_craica')
    list_filter = ('titulo','usuario',)

admin.site.register(Evento,EventoAdmin)
