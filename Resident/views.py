from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from Building.models import Announcement,Society,Dues
from Resident.models import Resident
from Account.models import User



def resident_dashboard(request):
    user_name = request.session.get('user_name')
    resident = Resident.objects.get(user_name=user_name)
    context = {
        'name': resident.name,
        'apt_number': resident.apartmentNumber.Apartment_number,
        'society': resident.building.society_name,
        'contact_info': resident.contactInformation
    }
    return render(request, 'resident_dashboard.html', context)



def account_view(request):
    return render(request,'account_view.html')


def display_announcements(request):
    # Assuming society is the current user's society
    user_name = request.session.get('user_name')
    print(user_name)
    resident = Resident.objects.get(user_name=user_name)
    print(resident)
    society = resident.building
    print(society.society_name)


    # Fetch announcements for the specific society and order them by creation date in descending order
    announcements = Announcement.objects.filter(society=society)
    print(announcements)
    return render(request, 'display_announcements.html', {'announcements': announcements})

def view_all_dues(request):
    user_name = request.session.get('user_name')
    resident = Resident.objects.get(user_name=user_name) 
    # Retrieve all dues from the database
    all_dues = Dues.objects.filter(building=resident.building, apartment_id=resident.apartmentNumber)

    return render(request, 'display_dues.html', {'all_dues': all_dues})

