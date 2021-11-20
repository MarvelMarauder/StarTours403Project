from django.shortcuts import render
from django.http import HttpResponse
from .models import Character

# Main travel page view
def travelPageView(request) :
    context = {
        "places_to_visit" : ["Arenal Volcano", "Manual Antonio National Park", "Monteverde Cloud Forest"]
    }
    return render(request, 'travelpages/travelpages.html', context)

def studentPageView(request) :
    data = Character.objects.all()

    context = {
        "our_students" : data
    }

    return render(request, 'travelpages/displayStudents.html', context)
# these will be our pages that will give details about the trip itself
def aboutPageView(request, trip_name, trip_length) :
    context = {
    "trip_name" : trip_name,
    "trip_length" : int(trip_length) + 2,
    "places_to_visit" : ["Arenal Volcano", "Manual Antonio National Park", "Monteverde Cloud Forest"]
    } 

    return render(request, 'travelpages/trippage.html', context) 