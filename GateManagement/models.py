from django.db import models
from django.utils import timezone
from Building.models import Society,Apartment # Assuming you have a Society model

# Create your models here.



class EmergencyInformation(models.Model):
    id = models.IntegerField(primary_key=True),
    type = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    contact_person_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} - {self.society}"
    
class VisitorLog(models.Model):
    visitor_id = models.IntegerField(primary_key=True),
    visitor_name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15)  # Assuming CNIC number is 15 characters long
    date_of_visit = models.DateField(default=timezone.now)
    entrance_time = models.TimeField(default=timezone.now)
    date_of_exit = models.DateField(default=timezone.now)
    exit_time = models.TimeField(blank=True, null=True)
    apartment_number_to_visit = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.visitor_name} - {self.apartment_number_to_visit} - {self.date_of_visit}"