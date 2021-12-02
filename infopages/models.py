from django.db import models
from django.db.models.deletion import DO_NOTHING
# Create your models here.
from travelpages.models import Customer, Character, TravelPlanet, Trip
class Customer2(models.Model):
    customer = models.ForeignKey(Customer, on_delete=DO_NOTHING)
