from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse
def index(request):
    # Use the direct path for the about page
    response = 'Rango says hey there partner!<br><a href="/rango/about/">About</a>'
    return HttpResponse(response)

def about(request):
    # Use the direct path for the index page
    response = 'Rango says here is the about page.<br><a href="/rango/">Index</a>'
    return HttpResponse(response)