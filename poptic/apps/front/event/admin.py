from django.contrib import admin
from poptic.apps.front.event.models import Event, Ticket


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'start'
    list_display = ('name', 'start')

class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'event')

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
