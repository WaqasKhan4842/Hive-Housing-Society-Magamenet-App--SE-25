from django.db import models
from Account.models import User
from Building.models import Society

# Create your models here.
class Gatekeeper(models.Model):
    id_number = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=100)
    shift_time_day = models.CharField(max_length=10)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    phone_number = models.CharField(max_length=15)
    current_status = models.CharField(max_length=100)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Society, on_delete=models.CASCADE)
    # You can add more fields as needed

    def __str__(self):
        return self.name