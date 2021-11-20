from django.db import models
from datetime import datetime, timedelta

from django.db.models.deletion import CASCADE

#there are a lot of null values for almost all of the fields in the data we've pulled off of the internet
#we should create models that can accept null values
#the length of the fields also varies greatly so they should be long fields


# Create your models here.
class TravelPlanet(models.Model):
    name = models.CharField(max_length=30)
    rotation_period = models.CharField(max_length=10)
    orbital_period = models.CharField(max_length=10)
    diameter = models.CharField(max_length=15)
    climate = models.CharField(max_length=15)
    gravity = models.CharField(max_length=20)
    terrain = models.CharField(max_length=20)
    surface_water = models.CharField(max_length=20)
    population = models.CharField(max_length=20)
    created_date = models.CharField(max_length=20)
    updated_date = models.CharField(max_length=20)
    url = models.CharField(max_length=30)
    #planetfakeid = models.CharField(max_length=20)
    # will have ID field and description field

    def __str__(self):
        return (self.name) #returns some value rather than just a record in the database

class Character(models.Model):
    name = models.CharField(max_length=30)
    height = models.CharField(max_length=4)
    mass = models.CharField(max_length=5)
    hair_color = models.CharField(max_length=30)
    skin_color = models.CharField(max_length=30)
    eye_color = models.CharField(max_length=30, blank=True)
    birth_year = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=15, blank=True)
    planet_id = models.ForeignKey(TravelPlanet, on_delete=models.CASCADE) # here is the reference to the home planet
    created_date = models.CharField(max_length=30, blank=True)
    updated_date = models.CharField(max_length=30, blank=True)
    url = models.CharField(max_length=50, blank=True)
    #characterfakeID = models.CharField(max_length=5, blank=False)
    #home_planet = models.ForeignKey(TravelPlanet, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name) 

class Customer(models.Model): #specify all of the attributes in the database
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13, blank=True)
    fav_character = models.ForeignKey(Character, default="Yoda", blank=True, on_delete=models.CASCADE)

    def __str__(self) : 
        return (self.full_name)



    # create an attribute (property) associated with the class but not stored in the database
    @property 
    def full_name(self) : # has the format of string (space) string %s %s
        return '%s %s' % (self.first_name, self.last_name) 

    #write a method

    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(Customer, self).save() #call the original save method

#make sure the travelsites app is referenced in the settings.py 



""" class Grade_level(models.Model) :
    class_level = models.CharField(max_length = 2, unique = True)
    description = models.CharField(max_length = 20)

    class Meta:
        db_table = "grade_level"

    def __str__(self):
        return (self.description)

class Student(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    class_level = models.ForeignKey(Grade_level, default="", verbose_name="student class", on_delete=models.DO_NOTHING, to_field="class_level")

    class Meta:
        db_table = "student"

    def __str__(self):
        return (self.first_name + " " +self.last_name) """