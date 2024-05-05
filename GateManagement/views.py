from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.
from .models import EmergencyInformation,VisitorLog
from Building.models import Society,Apartment
from Account.models import User
from GateKeeper.models import Gatekeeper


def add_emergency_information(request):
    if request.method == 'POST':
        # Extract data from the POST request
        type = request.POST.get('type')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        contact_person_name = request.POST.get('contact_person_name')
        organization = request.POST.get('organization')
        user_name = request.session.get('user_name')
        society = Society.objects.get(user_name=user_name)
        
        # Create EmergencyInformation object and save it to the database
        emergency_info = EmergencyInformation(
            type=type,
            contact=contact,
            email=email,
            contact_person_name=contact_person_name,
            organization=organization,
            society = society
        )
        emergency_info.save()
        
        return redirect('admin_dashboard')  # Redirect to a success page

    return render(request, 'emergency_create.html')




def display_emergency_information(request):
    # Dummy emergency contacts data
    emergency_contacts = None

    if request.method == 'GET':
        if 'emergency_type' in request.GET:
            emergency_type = request.GET.get('emergency_type')
            user_name = request.session.get('user_name')
            gatekeeper = Gatekeeper.objects.get(user_name=user_name)
            society = Society.objects.get(building_id=gatekeeper.building.building_id)
            # Assuming EmergencyInformation model is defined and contains relevant data
            emergency_contacts = EmergencyInformation.objects.filter(type=emergency_type,society=society)
            print(emergency_contacts)

    return render(request, 'list_emergency_contacts.html', {'emergency_contacts': emergency_contacts})

def trigger_emergency_call(request):
    # Dummy implementation for triggering an emergency call
    # You can implement your actual logic here, such as calling an external API, sending notifications, etc.
    # For now, let's return a simple response indicating that the call has been triggered.
    return HttpResponse("Emergency call triggered successfully!")

def enter_visitor(request):
    if request.method == 'POST':
        visitor_name = request.POST.get('visitor_name')
        cnic = request.POST.get('cnic')
        entrance_time = request.POST.get('entrance_time')
        apartment_number_to_visit = request.POST.get('apartment_number_to_visit')
        user_name = request.session.get('user_name')
        gatekeeper = Gatekeeper.objects.get(user_name=user_name)
        society = Society.objects.get(building_id=gatekeeper.building.building_id)
        
        # Fetch the apartment instance using the provided apartment number
        aprt = Apartment.objects.filter(Apartment_number=apartment_number_to_visit, building=society).first()

        # Check if apartment exists
        if not aprt:
            error_message = "Apartment is not Registered"
            return render(request, 'visitors_log.html', {'error_message': error_message})

        # Check if CNIC is valid
        if not cnic.isdigit() or len(cnic) != 13:
            error_message = "Invalid CNIC number"
            return render(request, 'visitors_log.html', {'error_message': error_message})

        # Automatically set the date of visit to today's date
        date_of_visit = timezone.now().date()

        # Create a new VisitorLog object
        VisitorLog.objects.create(
            visitor_name=visitor_name,
            cnic=cnic,
            date_of_visit=date_of_visit,
            entrance_time=entrance_time,
            apartment_number_to_visit=aprt,
            society=society
        )

        # Set success message in session
        request.session['success_message'] = 'Visitor successfully entered.'

        return redirect('gatekeeper_dashboard')  # Redirect to a success URL
    else:
        return render(request, 'visitors_log.html')
    

def update_exit_time(request):
    if request.method == 'POST':
        visitor_id = request.POST.get('visitor_id')
        exit_time = request.POST.get('exit_time')

        try:
            # Retrieve the VisitorLog object
            visitor = VisitorLog.objects.get(cnic=visitor_id)
        except VisitorLog.DoesNotExist:
            error_message = "Visitor with the specified ID does not exist."
            return render(request, 'visitors_log.html', {'error_message': error_message})

        # Check if exit time is already set
        if visitor.exit_time is not None:
            error_message = "Exit time is already set for this visitor."
            return render(request, 'visitors_log.html', {'error_message': error_message})

        # Update the exit time
        visitor.exit_time = exit_time
        visitor.save()

        return redirect('gatekeeper_dashboard.html')  # Redirect to a success URL
    else:
        return render(request, 'visitors_log.html')
