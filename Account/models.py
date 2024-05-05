from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=10)
    user_type = models.CharField(max_length=100)

class SocietyOwner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    cnic = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"