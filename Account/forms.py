from django import forms
from .models import User, SocietyOwner

class SocietyOwnerForm(forms.ModelForm):
    class Meta:
        model = SocietyOwner
        fields = ['first_name', 'last_name', 'phone_number', 'address']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'password', 'user_type']