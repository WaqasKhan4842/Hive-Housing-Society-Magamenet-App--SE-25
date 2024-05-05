from django.shortcuts import render,redirect,get_object_or_404
from Resident.models import Resident
from GateKeeper.models import Gatekeeper

# Create your views here.

def gatekeeper_dashboard(request):
    return render(request,'gatekeeper_dashboard.html')

def get_resident_info(request):
    if request.method == 'POST':
        user_name = request.session.get('user_name')
        gatekeeper = Gatekeeper.objects.get(user_name=user_name)
        society = gatekeeper.building
        ssn = request.POST.get('ssn')
        resident = Resident.objects.filter(building=society, SSN_Number=ssn).first()  # Use .first() to get the first resident or None
        if resident:
            return render(request, 'get_resident_info.html', {'resident': resident})
        else:
            # Resident does not exist in the specified society
            error_message = "Resident with the provided SSN does not exist in this society."
            return render(request, 'get_resident_info.html', {'error_message': error_message})
    else:
        return render(request, 'get_resident_info.html')
    

