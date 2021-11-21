from django.urls import path
from .views import infoPageView
from .views import characterPageView
from .views import planetPageView

urlpatterns = [
    #connecting to the different url methods
    path('', infoPageView, name = 'info'),
    path('character/', characterPageView, name = 'character'),
    path('planet/', planetPageView, name = 'planet'),

]