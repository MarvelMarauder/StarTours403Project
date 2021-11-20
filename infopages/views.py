from django.shortcuts import render
from django.http import HttpResponse

# main info page for all planets and organisms
def infoPageView(request) :
    return HttpResponse('Click Here to learn more about our fascinating creatures and planets!')

#page for individual organism information
def characterPageView(request, character_name) :
    sOutput = '<html><head><title>Character Watch</title></head><body><p style="color:red;"><h1>Welcome to our page about '+character_name+'</h1></p><p style="color:blue;">two</p><p style="font-size:50px;">three</p><ul><li>A</li><li>B</li><li>C</li></ul></body></html>'
    return HttpResponse(sOutput)

#page for individual planet information
def planetPageView(request, planet_name) :
    sOutput = '<html><head><title>Planetary Travel</title></head><body><p>Welcome to ' + planet_name + '</p></body></html>'
    return HttpResponse(sOutput)