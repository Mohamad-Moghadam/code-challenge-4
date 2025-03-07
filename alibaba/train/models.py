from django.db import models



class Customer(models.Model):
    
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    email = models.EmailField(null=True , blank=True)
    payment = models.BooleanField(default=False)
class Tarin():
    name = models.CharField(max_length=20)
    

class Reservation():
    pass

class 
