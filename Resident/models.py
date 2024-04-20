from django.db import models

# Create your models here.
class Resident(models.Model):
    Name =  models.CharField(max_length=100)
    Contact_Information = models.TextField()
    SSN_Number = models.CharField(primary_key=True, max_length=11)  # Assuming SSN is 9 digits long with optional dashes