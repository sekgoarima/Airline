from django.contrib import admin

from .models import Flight, Airline,Passenger

# Register your models here.
admin.site.register(Airline)
admin.site.register(Flight)
admin.site.register(Passenger)
