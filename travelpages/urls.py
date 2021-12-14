from django.urls import path
from .views import travelPageView, indexPageView, contactPageView, infoPageView, characterPageView
from .views import planetPageView, aboutPageView, customerPageView, updateCustPageView, deleteCustPageView, aboutUsPageView
from .views import custInfoPageView, updateCustomerPageView, addCustomerPageView, searchCharPageView, searchPlanetPageView

urlpatterns = [
    #main pages urls
    path('', indexPageView, name="index"),
    path('about/', aboutUsPageView, name = "about"),
    path('contact/', contactPageView, name = 'contact'),
    #connects us to our url functions
    path("travelpages/<trip_id>/", aboutPageView, name = "abouttrip"),
    path("cust/", customerPageView, name = 'customers'),
    path("addcust/", addCustomerPageView, name = 'addcust'),
    path("updatecust/<cust_id>", updateCustPageView, name = 'updateCustomer'),
    path('updatecustomer', updateCustomerPageView, name='updatecust'),
    path("deletecust/<cust_id>/", deleteCustPageView, name = 'deleteCustomer'),
    path("custinfo/<cust_id>/", custInfoPageView, name = 'customerinfo'),
    path("travelpages/", travelPageView, name="travelpages"),
    #infopages urls
    path('information/', infoPageView, name = 'info'),
    path('character/<char_id>/', characterPageView, name = 'character'),
    path('planet/<plan_id>', planetPageView, name = 'planet'),
    #searchpages urls
    path('searchCharacter/', searchCharPageView, name = 'searchchar'),
    path('searchPlanet/', searchPlanetPageView, name = 'searchplanet'),
]