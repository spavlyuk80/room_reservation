from django.contrib import admin

# Register your models here.
from .models import Room, Reservation, ExternalVisitor

admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(ExternalVisitor)
