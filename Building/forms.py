from django import forms
from .models import Society

class SocietyForm(forms.ModelForm):
    class Meta:
        model = Society
        fields = '__all__'  # You can specify the fields you want to include in the form here if needed
