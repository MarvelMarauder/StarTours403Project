from django.urls import path
from .views import contactPageView, indexPageView
from .views import aboutPageView

urlpatterns = [
    #connecting to the url methods for this application
    path('', indexPageView, name="index"),
    path('about/', aboutPageView, name = "about"),
    path('contact/', contactPageView, name = 'contact')
]