from django.shortcuts import render,redirect, get_object_or_404

from django.contrib import messages


from datetime import date
from django.db.models import F
from django.utils import timezone
from .forms import Announcement
from Building.models import Society,Apartment, Dues
from GateKeeper.models import Gatekeeper
from Account.models import User
from Resident.models import Resident


# Create your views here.

def amdin_dashboard(request):
    return render(request,'admindashboard.html')

def submit_notification(request):
    if request.method == 'POST':
        title = request.POST.get('notification_title')
        type = request.POST.get('notification_type')
        description = request.POST.get('notification_content')
        expiration_date = request.POST.get('expiration_date')
        
        # Check if the expiration date is in the past
        if expiration_date:
            expiration_date = date.fromisoformat(expiration_date)
            if expiration_date < timezone.now().date():
                error_message = "Expiration date cannot be in the past."
                return render(request, 'submit_notification.html', {'error_message': error_message, 'title': title, 'type': type, 'description': description, 'expiration_date': expiration_date})
        
        # Retrieve building_id from the current user's session
        user_name = request.session.get('user_name')
        society = Society.objects.get(user_name=user_name)
        
        # Create and save the announcement with building_id
        announcement = Announcement(title=title, type=type, description=description, expiration_date=expiration_date, society=society)
        announcement.save()
        
        # Render the same template with a success message
        success_message = "Successfully submitted."
        return render(request, 'submit_notification.html', {'success_message': success_message})
    else:
        return render(request, 'submit_notification.html')  # Render the form template

    


def add_gatekeeper(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        shift_timing = request.POST.get('shift_timing')
        phone_number = request.POST.get('phone_number')
        current_status = request.POST.get('current_status')
        user_name = request.POST.get('user_name')  # Assuming you get this from the form
        # Assuming you have access to the logged-in user's building
        user_name = request.session.get('user_name')
        society = Society.objects.get(user_name=user_name)

        gatekeeper = Gatekeeper.objects.create(name=name, shift_timing=shift_timing,
                                               phone_number=phone_number, current_status=current_status,
                                               user_name=user_name, building=society)
        return redirect('success_page')  # Change 'success_page' to the appropriate URL name
    else:
        return render(request, 'add_gatekeeper.html')  # Render the form template

def gatekeeper_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        shift_time_day = request.POST.get('shift_time_day')
        shift_start = request.POST.get('shift_start')
        shift_end = request.POST.get('shift_end')
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Create a new user
        user = User(user_name=username, password=password, user_type='Gatekeeper')
        user.save()
        user_name = request.session.get('user_name')
        society = Society.objects.get(user_name=user_name)
        
        # Create a new gatekeeper linked to the user
        gatekeeper = Gatekeeper(name=name, shift_time_day=shift_time_day, shift_start=shift_start, shift_end=shift_end,
                                phone_number=phone_number, current_status="Employed", user_name=user, building=society)
        gatekeeper.save()
        
        # Redirect to a success page or any other page as needed
        return redirect('admin_dashboard')  # Change 'success_page' to the appropriate URL name
    else:
        return render(request, 'gatekeeper_registration.html')  # Render the form template
    
def list_apartments(request):
    user_name = request.session.get('user_name')

    society = Society.objects.get(user_name=user_name)


     # Retrieve all residents associated with the building
    residents = Resident.objects.filter(building=society)




     # Create a dictionary to store apartment numbers and corresponding user names
    apartment_details = {}

   # Iterate over each resident to get their apartment number and user name
    for resident in residents:
        apartment_number = resident.apartmentNumber.Apartment_number

        user_name = resident.name


        # If the apartment number is not already in the dictionary, add it
        if apartment_number not in apartment_details:
            apartment_details[apartment_number] = []

        # Add the user name to the list of user names for the apartment number
        apartment_details[apartment_number].append(user_name)
        print(apartment_details)

    return render(request, 'list_apartments.html', {'apartment_details': apartment_details})

   
def view_dues(request, apartment_number):
    user_name = request.session.get('user_name')

    society = Society.objects.get(user_name=user_name)
    
    # Retrieve dues associated with the specified apartment
    dues = Dues.objects.filter(apartment_id=apartment_number, building=society)
    
    # Sort the dues based on status (False first) and then due_date
    dues = dues.order_by('status', 'due_date')

    return render(request, 'view_dues.html', {'dues': dues, 'apartment_number': apartment_number})

def add_dues(request, apartment_number):
    if request.method == 'POST':
        dues_type = request.POST.get('dues_type')
        amount = float(request.POST.get('amount'))
        due_date = request.POST.get('due_date')
        user_name = request.session.get('user_name')

        # Retrieve the society and apartment objects
        society = Society.objects.get(user_name=user_name)
        apartment = Apartment.objects.get(Apartment_number=apartment_number, building=society)

        # Validate due_date
        if due_date < timezone.now().strftime('%Y-%m-%d'):
            error_message = "Due date cannot be in the past."
            return render(request, 'add_dues.html', {'apartment_number': apartment_number, 'error_message': error_message})

        # Validate amount
        if amount < 0:
            error_message = "Amount cannot be negative."
            return render(request, 'add_dues.html', {'apartment_number': apartment_number, 'error_message': error_message})

        # Create and save the new dues object
        dues = Dues(
            dues_type=dues_type,
            status=False,  # Assuming all newly added dues have pending status
            amount=amount,
            due_date=due_date,
            apartment_id=apartment,
            building=society
        )
        dues.save()

        # Redirect to view_dues page with success message
        success_message = "Dues successfully added."
        return render(request, 'add_dues.html', {'apartment_number': apartment_number, 'success_message': success_message})

    return render(request, 'add_dues.html', {'apartment_number': apartment_number})

def delete_dues(request, due_id):
    # Retrieve the due object
    due = get_object_or_404(Dues, pk=due_id)
    
    # Delete the due
    due.delete()
    
    # Redirect to the view dues page
    return redirect('view_dues', apartment_number=due.apartment_id.Apartment_number)

def update_dues(request, due_id):
    # Retrieve the due object
    due = get_object_or_404(Dues, pk=due_id)
    
    if request.method == 'POST':
        # Get the new values from the request
        new_status = request.POST.get('update_status')
        new_amount = request.POST.get('update_amount')
        new_due_date = request.POST.get('update_due_date')
        if new_status == 'Paid':
            new_status = False
        else:
            new_status = True

        # Update the due object with the new values
        if new_status:
            due.status = new_status
        if new_amount:
            due.amount = new_amount
        if new_due_date:
            due.due_date = new_due_date

        # Save the changes to the due object
        due.save()

        # Redirect to the view dues page
        return redirect('view_dues', apartment_number=due.apartment_id.Apartment_number)

    return render(request, 'update_dues.html', {'due': due})
def logout_admin(request):
    return render(request, 'Login.html')

    


