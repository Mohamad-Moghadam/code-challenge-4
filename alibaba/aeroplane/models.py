from django.db import models
from train.models import Customer

class Reservations(models.Model):
    user = models.ForeignKey(to = Customer)
    time = models.DateTimeField(auto_now_add = True)
    passengers = models.IntegerField()
    one_way = models.BooleanField()
    departure_time = models.DateField()
    return_time = models.DateField(default = None)
    destination_city = models.CharField(max_length = 100)
    starting_city = models.CharField(max_length = 100)

class 