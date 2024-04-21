from django.shortcuts import render,redirect
from .models  import *
from .forms import SocietyForm

# Create your views here.
def Add_Amenity(request):
    if request.method == "POST":
        data = request.POST
        amenity_name = data.get('amenity_name')
        description = data.get('description')
        status = data.get('status')
        location = data.get('location')
        capacity = data.get('capacity')
        opening_hrs = data.get('opening_hrs')
        reservation_fees = data.get('reservation_fees')
        maintenance = data.get('maintenance')
        availability = data.get('availability') == 'on'  # Convert to boolean
        print("Amenity Name:", amenity_name)
        print("Description:", description)
        print("Status:", status)
        print("Location:", location)
        print("Capacity:", capacity)
        print("Opening Hours:", opening_hrs)
        print("Reservation Fees:", reservation_fees)
        print("Maintenance:", maintenance)
        print("Availability:", availability)
         # Create an instance of Amenities model with the provided data
        new_amenity = Amenities(
            amenityName=amenity_name,
            Description=description,
            amenityStatus=status,
            location=location,
            capacity=capacity,
            openingHrs=opening_hrs,
            reservationFees=reservation_fees,
            maintenance=maintenance,
            availability=availability
        )
        # Save the new amenity to the database
        new_amenity.save()

    return render(request,"addAmenity.html")




def add_society(request):
    if request.method == 'POST':
        form = SocietyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Resident_Dashboard/')  # Redirect to a success page
    else:
        form = SocietyForm()
    return render(request, 'add_society.html', {'form': form})


  