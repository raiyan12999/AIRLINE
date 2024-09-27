from django.shortcuts import render
from .models import *
from flights.views import *


# Create your views here.

def index(request):
    flights = Flight.objects.all()
    if request.method == "POST":

        First_name = request.POST["first_name"]
        Last_name = request.POST["last_name"]
        passengers = Passenger.objects.filter(first=First_name, last=Last_name)

        if passengers.exists():  
            passenger = passengers.first()
        else:
            # If no matching passenger is found, create a new one
            passenger = Passenger(first=First_name, last=Last_name)
            passenger.save()  # Save the new passenger to the database

        flight_id = request.POST.get("Flight")
        fflight = Flight.objects.get(id=flight_id)

        # Add the flight to the passenger's list of flights
        passenger.flight.add(fflight)

        context = {
            "flights" : flights,
            "message" : "Booking Successful!"
        }

        return render(request, "booking/index.html", context)
    # else:
    #     First_name = "Nothing"
    #     Last_name = "Nothing"
    #     Person = People.objects.create(first = First_name, last = Last_name)
    #     Person.save()

    # context = {
    #     "first_name": First_name,
    #     "last_name" : Last_name,
    #     "person" : Person
    # }

    context = {
        "flights" : flights
    }
    return render(request, "booking/index.html", context)
