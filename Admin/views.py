from django.shortcuts import render,redirect

from django.contrib import messages
from .forms import ResidentRegistrationForm, UserRegistrationForm
# Create your views here.

def Admin_Dashboard(request):
    return render(request,'admindashboard.html')



from django.contrib import messages

def register_resident(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        resident_form = ResidentRegistrationForm(request.POST)
        if user_form.is_valid() and resident_form.is_valid():
            user = user_form.save()
            resident = resident_form.save(commit=False)
            resident.user = user
            resident.save()
            messages.success(request, 'Resident registered successfully!')
            return redirect('account')
        else:
            # Print form errors
            print(user_form.errors)
            print(resident_form.errors)
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        user_form = UserRegistrationForm()
        resident_form = ResidentRegistrationForm()
    context = {
        'user_form': user_form,
        'resident_form': resident_form,
    }
    return render(request, 'add_resident.html', context)

