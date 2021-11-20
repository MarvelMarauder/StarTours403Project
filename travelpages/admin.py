from django.contrib import admin

# Register your models here.
from .models import Character, Customer, TravelPlanet

admin.site.register(Customer)
admin.site.register(TravelPlanet)
admin.site.register(Character)