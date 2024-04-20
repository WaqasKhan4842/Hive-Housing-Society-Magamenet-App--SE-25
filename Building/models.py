from django.db import models
from .models import *
from Resident.models import Resident



# Create your models here.
class Dues(models.Model):
    dues_type =  models.CharField(max_length=100)
    status = models.BooleanField()

class Apartment(models.Model):
    Apartment_number = models.IntegerField()
    Floor_Number = models.IntegerField()
    No_of_Rooms = models.IntegerField()
    dues = models.ForeignKey(Dues, on_delete= models.CASCADE)

class Reservations(models.Model):
    reservationId = models.AutoField(primary_key=True)
    amenity = models.OneToOneField('Amenities', on_delete=models.CASCADE)
    reservationDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    residentSsn = models.ForeignKey(Resident, to_field='SSN_Number', on_delete=models.CASCADE)

    
    def __str__(self):
        return f"Reservation ID: {self.reservationId}"

class Amenities(models.Model):
    amenityId = models.AutoField(primary_key=True)
    amenityName = models.CharField(max_length=100)
    Description = models.TextField()
    amenityStatus = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    openingHrs = models.CharField(max_length=100)
    reservationFees = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming fees are decimal
    maintenance = models.TextField()
    availability = models.BooleanField(default=True)  # Assuming availability is a boolean field
    
    def __str__(self):
        return self.amenityName

