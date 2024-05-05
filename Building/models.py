from django.db import models
from Resident.models import Resident
from Account.models import User

class Society(models.Model):
    building_id = models.AutoField(primary_key=True, default=0)
    society_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    total_apartments = models.PositiveIntegerField()
    contact_info = models.CharField(max_length=15)
    number_of_floors = models.PositiveIntegerField()
    number_of_blocks = models.PositiveIntegerField()
    start_block = models.CharField(max_length=1)
    end_block = models.CharField(max_length=1)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Society: {self.society_name}, Address: {self.street_address}, {self.city}, {self.province}, {self.postal_code}"


class Apartment(models.Model):
    Apartment_number = models.IntegerField(primary_key=True)
    Floor_Number = models.IntegerField()
    No_of_Rooms = models.IntegerField()
    building = models.ForeignKey(Society, on_delete=models.CASCADE)
    
class Dues(models.Model):
    dues_type = models.CharField(max_length=100)
    status = models.BooleanField()
    amount = models.FloatField()
    due_date = models.DateField()
    apartment_id = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    building = models.ForeignKey(Society, on_delete=models.CASCADE)



    def __str__(self):
        return f"Apartment Number: {self.apartment_number}, Floor Number: {self.floor_number}, Society: {self.building.society_name}"

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
    amenityId = models.AutoField(primary_key=True,default=0)
    amenityName = models.CharField(max_length=100)
    Description = models.TextField()
    amenityStatus = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    openingHrs = models.CharField(max_length=100)
    reservationFees = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    building = models.ForeignKey(Society, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.amenityName
    

class Announcement(models.Model):
    announcement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()  # Change to DateField
    society = models.ForeignKey('Society', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Complaint(models.Model):
    # Attributes of the Complaint model
    complaint_id = models.AutoField(primary_key=True)  # Change to AutoField for auto-incrementing
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    complaint_type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    society = models.ForeignKey('Society', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='complaint_images/', blank=True, null=True)
    status = models.CharField(max_length=100)


    def __str__(self):
        return self.name + " - " + self.complaint_type