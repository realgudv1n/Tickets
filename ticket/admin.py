from django.contrib import admin

from .models import Ticket, TicketMessage

admin.site.register(Ticket)
admin.site.register(TicketMessage)
