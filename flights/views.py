from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    context = {
        "flights" : Flight.objects.all()
        
    }

    return render(request, 'flights/index.html', context = context)

def detail(request, pk):
    flight = Flight.objects.get(id = pk)
    #passenger = Passenger.objects.filter(flight.id)
    context = {
        "ID": pk,
        "flights" : Flight.objects.all(),
        "flight" : flight,
        "passengers" : Passenger.objects.all(),
        "pass" : flight.passengers.all()
        
    }
    return render(request, "flights/detail.html", context = context)

