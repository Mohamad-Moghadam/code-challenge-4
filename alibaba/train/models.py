from django.db import models
from aeroplane.models import Reservations


class Customer(models.Model):
    
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    email = models.EmailField(null=True , blank=True)
    payment = models.BooleanField(default=False)
    
class Tarin(models.Model):
    
    
    name = models.CharField(max_length=20)
    entrance_date = models.DateTimeField(auto_now_add=True)
    capacity = models.PositiveIntegerField()
    rate = models.CharField(max_length=10)
    code = models.CharField(max_length=10,unique=True)
    carrage =models.CharField(max_length=10)
    





