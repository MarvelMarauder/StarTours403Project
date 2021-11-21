from django.shortcuts import render
from django.http import HttpResponse

# main info page for all planets and organisms
def infoPageView(request) :
    return render(request, 'infopages/info.html')

#page for individual organism information
def characterPageView(request) :
    return render(request, 'infopages/character.html')

#page for individual planet information
def planetPageView(request) :
    return render(request, 'infopages/planet.html')