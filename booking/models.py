from django.db import models
from flights.models import *

# Create your models here.

class People(models.Model):
    first = models.CharField(max_length=65)
    last = models.CharField(max_length = 65)

    def __str__(self):
        return f"{self.first} {self.last}"