from django.contrib import admin

# Register your models here.
from .models import Character, Customer, TravelPlanet, Trip

admin.site.register(Customer)
admin.site.register(TravelPlanet)
admin.site.register(Character)
admin.site.register(Trip)
#admin.site.register()