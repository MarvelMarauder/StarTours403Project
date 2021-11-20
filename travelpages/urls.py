from django.urls import path
from .views import studentPageView, travelPageView
from .views import aboutPageView

urlpatterns = [
    #connects us to our url functions
    path("<trip_name>/<trip_length>/", aboutPageView, name = "about"),
    path("stud/", studentPageView, name = 'students'),
    path("", travelPageView, name="travelpages"),
]