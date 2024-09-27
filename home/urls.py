from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name='home'),
    path("", views.register, name='register'),
    path("login/", views.login_page, name= 'login'),
    path("logout/", views.logout_page, name='logout'),
    path("adminpage/", views.admin_page, name='adminpage'),
    path("editair/", views.add_airport, name= 'add_airport'),
    path("editflight/", views.add_flight, name= 'add_flight')
]