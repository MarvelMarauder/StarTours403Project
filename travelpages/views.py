from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Trip, TravelPlanet

# Main travel page view
def travelPageView(request) :
    data = Trip.objects.all

    context = {
        "available_trips" : data
    }
    return render(request, 'travelpages/travelpages.html', context)

def studentPageView(request) :
    data = Character.objects.all()

    context = {
        "our_students" : data
    }

    return render(request, 'travelpages/displayStudents.html', context)
# these will be our pages that will give details about the trip itself
def aboutPageView(request, trip_name) :
    data = Trip.objects.get(id=trip_name)
    context = {
        "this_trip" : data
    } 

    return render(request, 'travelpages/trippage.html', context) 