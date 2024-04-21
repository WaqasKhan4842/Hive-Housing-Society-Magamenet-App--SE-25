from django.db import models
from Resident.models import Resident

class Society(models.Model):
    building_id = models.AutoField(primary_key=True)
    society_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    total_apartments = models.PositiveIntegerField()
    owner_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=15)
    number_of_floors = models.PositiveIntegerField()
    number_of_blocks = models.PositiveIntegerField()
    start_block = models.CharField(max_length=1)
    end_block = models.CharField(max_length=1)
    number_of_apartments_each_floor = models.PositiveIntegerField()

    def __str__(self):
        return f"Society: {self.society_name}, Address: {self.street_address}, {self.city}, {self.province}, {self.postal_code}"

    def __str__(self):
        return f"Society: {self.society_name}, Address: {self.address}"

class Dues(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE, default=1)  # Provide a default value here
    dues_type = models.CharField(max_length=100)
    status = models.BooleanField()

class Apartment(models.Model):
    Apartment_number = models.IntegerField(primary_key=True)
    Floor_Number = models.IntegerField()
    No_of_Rooms = models.IntegerField()
    dues = models.ForeignKey(Dues, on_delete=models.CASCADE)

class Reservations(models.Model):
    reservationId = models.AutoField(primary_key=True)
    amenity = models.OneToOneField('Amenities', on_delete=models.CASCADE)
    reservationDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)

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
    reservationFees = models.DecimalField(max_digits=10, decimal_places=2)
    maintenance = models.TextField()
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.amenityName
