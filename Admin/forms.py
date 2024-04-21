from django import forms
from Resident.models import *
from Account.models import *

class ResidentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['name', 'contactInformation', 'SSN_Number', 'apartmentNumber', 'currentStatus']
        # You can adjust the fields as needed

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'password']
        # You can adjust the fields as needed
