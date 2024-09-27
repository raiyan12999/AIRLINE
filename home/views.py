from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from flights.models import *

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    if request.method == "POST":
        key = request.POST.get("key")
        access = 12999

        if key is None:
            context = {"key": "Access denied: No key provided"}
            return render(request, "home/home.html", context)
        try:
            key = int(key)
        except ValueError:
            context = {"key" : "access denied"}
            return render(request, "home/home.html", context)
        if key == access:
            return redirect('/adminpage/')
        else:
            context = {"key" : "access denied"}
            return render(request, "home/home.html", context)
    return render(request, "home/home.html")



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")

        if not username:
            context = {"x": "Username is required"}
            return render(request, "home/register.html", context)

        if not firstname or not lastname or not password:
            context = {"x": "All fields are required"}
            return render(request, "home/register.html", context)

        user = User.objects.filter(username = username)
        if user.exists():
            context = {
                "x":"username already exists"
            }
            return render(request, "home/register.html", context)
        
        user = User.objects.create(
            first_name = firstname,
            last_name = lastname,
            username = username 
        )

        user.set_password(password)
        user.save()
        return redirect('/login/')

        # context = {
        #     'username' : username,
        #     'firstname': firstname,
        #     'lastname' : lastname
        # }

        # return render(request, "home/login.html", context)
    return render(request, "home/register.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        if user is None:
            context = {'x':"invalid username or password"}
            return render(request, "home/login.html", context)         
        else:
            login(request, user)
            return redirect("/home/")
            
    return render(request, "home/login.html")

def logout_page(request):
    logout(request)
    return redirect('/login/')

def admin_page(request):
    return render(request, "home/admin.html")


def add_airport(request):
    if request.method == "POST":
        city = request.POST.get("city")
        code = request.POST.get("code")

        # Check if 'code' is missing or empty
        if not code:
            context = {"message": "Airport code is required!"}
            return render(request, "home/add_airport.html", context)

        # Check if 'city' is missing or empty
        if not city:
            context = {"message": "City name is required!"}
            return render(request, "home/add_airport.html", context)

        # Create the airport
        try:
            airport = Airport.objects.create(city=city, code=code)
            airport.save()
            context = {"message": "New Airport Added!"}
        except Exception as e:
            # Handle any other potential errors
            context = {"message": f"An error occurred: {str(e)}"}

        return render(request, "home/add_airport.html", context)
    return render(request, "home/add_airport.html")


def add_flight(request):
    airports = Airport.objects.all()
    if request.method == "POST":
        airport1_id = request.POST.get("origin")
        airport2_id = request.POST.get("destination")
        duration = request.POST.get("duration")

        try:
            airport1 = Airport.objects.get(id = airport1_id)
            airport2 = Airport.objects.get(id = airport2_id)
        
        except Airport.DoesNotExist:
             context = {
                 'airports' : airports,
                 'message' : 'one or more airport does not exist'
             }
             return render(request, "home/add_flights.html", context)
       
        
        flight = Flight(origin = airport1, destination = airport2, duration = duration)
        flight.save()

        context = {
            'airports':airports,
            'message' : 'flight added successfully'
        }

        return render(request, "home/add_flights.html", context)
    context = {'airports':airports}
    return render(request, "home/add_flights.html", context)