from django.shortcuts import render
from django.http import HttpResponse
from travelpages.models import Customer, Trip, TravelPlanet, Character
from .models import Customer2

# main info page for all planets and organisms
def infoPageView(request) :
    data = Customer.objects.all()
    context = {
        "characters" : data
    }
    return render(request, 'infopages/info.html', context)

#page for individual organism information
def characterPageView(request) :
    return render(request, 'infopages/character.html')

#page for individual planet information
def planetPageView(request) :
    return render(request, 'infopages/planet.html')