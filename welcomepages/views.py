from django.shortcuts import render
from django.http import HttpResponse

# Main welcome page
def indexPageView(response) :
    return render(response, "welcomepages/index.html")

# about page for all to see
def aboutPageView(response) :
    return render(response, "welcomepages/about.html")
    
# contact page in case someone has complaints (they won't)
def contactPageView(response) :
    return HttpResponse("Welcome to our contact page! Please input your information and we'll be in touch with you as soon as possible.")
