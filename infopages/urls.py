from django.urls import path
from .views import infoPageView
from .views import organismPageView
from .views import planetPageView

urlpatterns = [
    #connecting to the different url methods
    path('', infoPageView, name = 'info'),
    path('organism/<organism_name>/', organismPageView, name = 'organism'),
    path('planet/<planet_name>/', planetPageView, name = 'planet'),

]