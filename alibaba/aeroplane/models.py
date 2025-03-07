from django.db import models
from train.models import Customer, Train



class Flights(models.Model):
    user = models.ForeignKey(to = Customer)
    time = models.DateTimeField(auto_now_add = True)
    passengers = models.IntegerField()
    one_way = models.BooleanField()
    departure_time = models.DateField()
    return_time = models.DateField(default = None)
    destination_city = models.CharField(max_length = 100)
    starting_city = models.CharField(max_length = 100)
    aeroplane_capacity = models.IntegerField()
    abroad_flight = models.BooleanField()
    seat = models.IntegerField()

class Reservations(models.Model):
    aeroplane_ticket = models.ForeignKey(to = Flights, on_delete = Flights, "aeroplane")
    train_ticket = models.ForeignKey(to = Train, on_delete = Train, "train_ticket")
    bus_ticket = models.ForeignKey(to = Bus, on_delete = Bus, "bus_ticket")