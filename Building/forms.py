from django import forms
from .models import Society,Apartment, Dues

class SocietyForm(forms.ModelForm):
    class Meta:
        model = Society
        fields = '__all__'  # You can specify the fields you want to include in the form here if needed




class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['Apartment_number', 'Floor_Number', 'No_of_Rooms']

class DuesForm(forms.ModelForm):
    class Meta:
        model = Dues
        fields = ['dues_type', 'status']

