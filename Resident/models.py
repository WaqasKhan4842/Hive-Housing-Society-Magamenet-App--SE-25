from django.db import models
from Account.models import User


# Create your models here.
class Resident(models.Model):
    name = models.CharField(max_length=100)
    contactInformation = models.TextField()
    SSN_Number = models.CharField(primary_key=True, max_length=11)  # Assuming SSN is 9 digits long with optional dashes
    apartmentNumber = models.ForeignKey('Building.Apartment', on_delete=models.CASCADE)
    currentStatus = models.CharField(max_length=100)  # You can adjust the max_length as needed
    building = models.ForeignKey('Building.Society', on_delete=models.CASCADE)  # Foreign key association with Building
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='resident_pictures/', null=True, blank=True)  # Picture field

