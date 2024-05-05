from django.shortcuts import render,redirect
from .models  import *
from django.contrib import messages
from django.http import HttpResponse
from .forms import SocietyForm,ApartmentForm,DuesForm
from Account.models import User
from Building.models import Society,Resident


def addAmenity(request):
    if request.method == 'POST':
        amenity_name = request.POST.get('amenity_name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        location = request.POST.get('location')
        capacity = request.POST.get('capacity')
        opening_hrs = request.POST.get('opening_hrs')
        reservation_fees = request.POST.get('reservation_fees')
        maintenance = request.POST.get('maintenance')
        availability = request.POST.get('availability') == 'true'  # Convert 'true' string to boolean
        user_name = request.session.get('user_name')
        society = Society.objects.get(user_name=user_name)
        # Create Amenity object
        amenity = Amenities(
            amenityName=amenity_name,
            Description=description,
            amenityStatus=status,
            location=location,
            capacity=capacity,
            openingHrs=opening_hrs,
            reservationFees=reservation_fees,
            availability=availability,
            building=society
        )
        amenity.save()
        print('successfully saved')

        # Redirect to a success page or any other page as needed
        return redirect('admin_dashboard')  # Change 'success_page' to the appropriate URL name
    else:
        return render(request, 'addAmenity.html')  # Render the form template




def add_society(request):
    if request.method == 'POST':
        form = SocietyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Resident_Dashboard/')  # Redirect to a success page
    else:
        form = SocietyForm()
    return render(request, 'add_society.html', {'form': form})

def apartment_registration(request):
    if request.method == 'POST':
        # Handle apartment registration form submission
        apartment_number = request.POST.get('apartment_number')
        floor_number = request.POST.get('floor_number')
        no_of_rooms = request.POST.get('no_of_rooms')

       

        # Fetch the building_id based on the current user's user_name
        user_name = request.session.get('user_name')
        society = Society.objects.get(user_name=user_name)
        building_id = society.building_id
         # Query the database to check if the apartment number already exists
        if Apartment.objects.filter( Apartment_number=apartment_number,building=building_id).exists():
            error_message = "Apartment number already exists. Please choose a different apartment number."
            return render(request, 'apartment_registration.html', {'error_message': error_message})

        # Store apartment registration data in session
        request.session['apartment_registration_data'] = {
            'apartment_number': apartment_number,
            'floor_number': floor_number,
            'no_of_rooms': no_of_rooms,
            'building_id': building_id,
        }

        # Redirect to resident registration form
        return redirect('resident_registration')
    else:
        # Render apartment registration form
        return render(request, 'apartment_registration.html')

def resident_registration(request):
    if request.method == 'POST':
        # Handle resident registration form submission
        name = request.POST.get('name')
        contact_information = request.POST.get('contactInformation')
        ssn_number = request.POST.get('SSN_Number')
        user_name = request.POST.get('username')
        password = request.POST.get('password')

      
        current_status = request.POST.get('currentStatus')
        picture = request.FILES.get('picture')  # Get the uploaded picture file
        
        # Get the building_id from session data
        apartment_data = request.session.get('apartment_registration_data')

        building_id = apartment_data['building_id']
        new_user = User(user_name=user_name, password=password, user_type='Resident')
        new_user.save()
        
        # Save apartment data
        apartment = Apartment(
            Apartment_number=apartment_data['apartment_number'],
            Floor_Number=apartment_data['floor_number'],
            No_of_Rooms=apartment_data['no_of_rooms'],
            building_id=building_id
        )
        apartment.save()
        curr_user =  request.session.get('user_name')
        user = User.objects.get(user_name=curr_user)
        # Save resident data
        resident = Resident(
            name=name,
            contactInformation=contact_information,
            SSN_Number=ssn_number,
            apartmentNumber=apartment,
            currentStatus=current_status,
            building_id=building_id,
            user_name=new_user,
            picture=picture
        )
        resident.save()
        
        # Clear session data except for user login credentials
        user_data = {
            'username': request.user.username,
        }
        request.session.clear()
        request.session.update(user_data)
        
        # Redirect to success page or any other page as needed
        return redirect('admin_dashboard')
    else:
        # Render resident registration form
        return render(request, 'resident_registration.html')
    
def lodge_complaint(request):
    if request.method == 'POST':
        complaint_type = request.POST.get('complaint_type')
        description = request.POST.get('description')
        
        # Check if an image was uploaded
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None
        
        user_name = request.session.get('user_name')
        user =  User.objects.get(user_name=user_name)
        resident = Resident.objects.get(user_name=user_name)
        
        # Create a Complaint object and save it to the database
        complaint = Complaint(resident=resident, complaint_type=complaint_type, description=description, society=resident.building, image=image,status="Pending")
        complaint.save()
        
        # Add a success message
        messages.success(request, 'Complaint submitted successfully!')
        
        return redirect('resident_dashboard')  # Redirect to the resident dashboard after submission
    
    # If not a POST request, render the complaint submission form
    return render(request, 'file_complaint.html')


def complaints_list(request):
    user_name = request.session.get('user_name')
    society = Society.objects.get(user_name=user_name)
    
    # Retrieve all complaints associated with the society
    complaints = Complaint.objects.filter(society=society)

    # Pass the complaints data to the template for rendering
    return render(request, 'track_complaints.html', {'complaints': complaints})
  