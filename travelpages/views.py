from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Trip, TravelPlanet, Customer

# Main welcome page
def indexPageView(response) :
    return render(response, "travelpages/index.html")

# about page for all to see
def aboutUsPageView(response) :
    return render(response, "travelpages/about.html")
    
# contact page in case someone has complaints (they won't)
def contactPageView(response) :
    return HttpResponse("Welcome to our contact page! Please input your information and we'll be in touch with you as soon as possible.")

# Main travel page view
def travelPageView(request) :
    data = Trip.objects.all()

    context = {
        "available_trips" : data
    }
    return render(request, 'travelpages/travelpages.html', context)

def customerPageView(request) :
    data = Customer.objects.all()

    context = {
        "cust" : data
    }

    return render(request, 'travelpages/customers.html', context)

def addCustomerPageView(request) :
    if request.method == 'POST' :
        customer = Customer()

        #customer.id = request.POST['id']
        customer.first_name = request.POST['first_name'] #these store the inputs from the form       
        customer.last_name = request.POST['last_name']
        customer.user_name = request.POST['username']
        customer.password = request.POST['password']
        customer.email = request.POST['email']
        customer.phone = request.POST['phone']
        customer.fav_character_id = request.POST['favchar']

        customer.save()

        return customerPageView(request)
    else :
        chars = Character.objects.all()
        context = {
            "char" : chars
        }
        return render(request, 'travelpages/addCustomer.html', context)

def updateCustPageView(request, cust_id) : #add update functionality
    data = Customer.objects.get(id = cust_id)
    chars = Character.objects.all()
    trips = Trip.objects.all()

    avail_trips = Trip.objects.exclude(id__in=data.cust_trips.all())
    context = {
        "cust" : data,
        "char" : chars,
        "trip" : avail_trips,
    }
    return render(request, 'travelpages/updateCustomer.html', context)

def updateCustomerPageView(request) :
     if request.method == 'POST' :
        id = request.POST['id']
        #favchar = request.POST['favchar']

        customer = Customer.objects.get(id=id)
        #char = Character.objects.get(name = favchar)

        customer.first_name = request.POST['first_name'] #these store the inputs from the form       
        customer.last_name = request.POST['last_name']
        customer.user_name = request.POST['username']
        customer.password = request.POST['password']
        customer.email = request.POST['email']
        customer.phone = request.POST['phone']
        customer.fav_character_id = request.POST['favchar']

        if request.POST['trip'] != '':
            customer.cust_trips.add(request.POST['trip'])

        customer.save()

        return customerPageView(request)


def deleteCustPageView(request, cust_id) : #delete functionality
    data = Customer.objects.get(id = cust_id)
    data.delete()

    return customerPageView(request)

def custInfoPageView(request, cust_id) :
    data = Customer.objects.get(id = cust_id)
    sQuery = "select travelpages_customer.id, travelpages_travelplanet.name from travelpages_customer\
        inner join travelpages_customer_cust_trips on travelpages_customer.id = travelpages_customer_cust_trips.customer_id\
        inner join travelpages_trip on travelpages_customer_cust_trips.trip_id = travelpages_trip.id\
        inner join travelpages_travelplanet on travelpages_trip.planet_id = travelpages_travelplanet.id\
        Where travelpages_customer.id = " + cust_id + "\
        "

    data1 = Trip.objects.raw(sQuery)
    context = {
        "cust" : data,
        "ctrip" : data1
    }
    return render(request, 'travelpages/customerInfo.html', context)


# these will be our pages that will give details about the trip itself
def aboutPageView(request, trip_id) :
    data = Trip.objects.get(id=trip_id)

    id = TravelPlanet.objects.get(id = data.planet_id)

    sQuery = "select travelpages_character.id, travelpages_character.name from travelpages_character\
                where travelpages_character.planet_id = " + str(data.planet_id)

    data1 = Character.objects.raw(sQuery)

    context = {
        "this_trip" : data,
        "planet" : id,
        "chars" : data1
    } 

    return render(request, 'travelpages/trippage.html', context) 

# main info page for all planets and organisms
def infoPageView(request) :
    char = Character.objects.all()
    planet = TravelPlanet.objects.all()
    
    context = {
        "characters" : char,
        "planets" : planet
    }
    return render(request, 'travelpages/info.html', context)

def searchCharPageView(request) :
    sName = request.GET['char_name'].upper()
    sGender = request.GET['gender']
    sQuery = 'select distinct travelpages_character.id, travelpages_character.name, travelpages_character.planet_id from\
        travelpages_character, travelpages_travelplanet\
        where travelpages_character.planet_id = travelpages_travelplanet.id'
    if sName != '' :
        sQuery += " AND upper(travelpages_character.name) like '" + sName + "%%'" 
    if sGender != '' :
        sQuery += " AND gender = '" + sGender + "'" 
    sQuery += ' ORDER BY travelpages_character.name'

    data = Character.objects.raw(sQuery)

    context = {
        "characters" : data,
    }
    return render(request, 'travelpages/info.html', context) 

def searchPlanetPageView(request) :

    sPlanetName = request.GET['plan_name'].upper()
    sQuery = 'select distinct travelpages_travelplanet.id, travelpages_travelplanet.name, population\
        from travelpages_character, travelpages_travelplanet\
        where travelpages_character.planet_id = travelpages_travelplanet.id'
    if sPlanetName != '' :
        sQuery += " AND upper(travelpages_travelplanet.name) like '" + sPlanetName + "%%'" 
        sQuery += ' ORDER BY travelpages_travelplanet.name'
    
    data = Character.objects.raw(sQuery)
    
    context = {
        "planets" : data,
    }
    return render(request, 'travelpages/info.html', context) 

#page for individual organism information
def characterPageView(request, char_id) :
    data = Character.objects.get(id=char_id)
    context = {
        "character" : data
    }
    return render(request, 'travelpages/character.html', context)

#page for individual planet information
def planetPageView(request, plan_id) :
    data = TravelPlanet.objects.get(id=plan_id)

    sQuery = "select travelpages_character.id, travelpages_character.name from travelpages_character\
        where travelpages_character.planet_id = " + str(plan_id)

    data1 = Character.objects.raw(sQuery)
    
    context = {
        "planet" : data,
        "chars" : data1
    }
    return render(request, 'travelpages/planet.html', context)