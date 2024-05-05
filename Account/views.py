from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import User,SocietyOwner
from Building.models import Society
from django.core.exceptions import ValidationError




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  User.objects.get(user_name=username,password=password)
        request.session['user_name'] = user.user_name
        print(user.user_name, user.password, user.user_type)
        if user is not None:
            print('User is not None')
            # Redirect based on user_type
            if user.user_type == 'Admin':
                print('I am in Admin')
                return redirect('admin_dashboard')
            elif user.user_type == 'Resident':
                return redirect('resident_dashboard')
            elif user.user_type == 'Gatekeeper':
                return redirect('gatekeeper_dashboard')
        else:
            return render(request, 'Login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'Login.html')



def reg_step1(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        cnic = request.POST.get('cnic')

        # Validate form data
        
        # Check if user with the same username already exists in User model
        if User.objects.filter(user_name=user_name).exists():
            print("Error!!!!!")
            return render(request, 'society_owner_registration.html', {'error_message': 'User with this username already exists.'})

        # Check if CNIC already exists in SocietyOwner model
        if SocietyOwner.objects.filter(cnic=cnic).exists():
            return render(request, 'society_owner_registration.html', {'error_message': 'A user with this CNIC already exists.'})

        # Store form data in session
        request.session['user_name'] = user_name
        request.session['password'] = password
        request.session['user_type'] = 'Admin'
        request.session['first_name'] = first_name
        request.session['last_name'] = last_name
        request.session['phone_number'] = phone_number
        request.session['address'] = address
        request.session['cnic'] = cnic

        return redirect('reg_step2')
    else:
        return render(request, 'society_owner_registration.html', {'user_name': request.session.get('user_name', '')})

def reg_step2(request):
    if request.method == 'POST':
        # Store form data in session
        society_name = request.POST.get('society_name')
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        province = request.POST.get('province')
        postal_code =  request.POST.get('postal_code')
        total_apartments = request.POST.get('total_apartments')
        contact_info = request.POST.get('contact_info')
        number_of_floors = request.POST.get('number_of_floors')
        number_of_blocks = request.POST.get('number_of_blocks')
        start_block = request.POST.get('start_block')
        end_block= request.POST.get('end_block')

        request.session['society_name'] = society_name
        request.session['street_address'] = street_address
        request.session['city'] =  city
        request.session['province'] = province
        request.session['postal_code'] =  postal_code
        request.session['total_apartments'] =  total_apartments
        request.session['contact_info'] = contact_info
        request.session['number_of_floors'] = number_of_floors
        request.session['number_of_blocks'] = number_of_blocks
        request.session['start_block'] = start_block
        request.session['end_block'] = end_block

        print(f"Society Name: {society_name}\n"
      f"Street Address: {street_address}\n"
      f"City: {city}\n"
      f"Province: {province}\n"
      f"Postal Code: {postal_code}\n"
      f"Total Apartments: {total_apartments}\n"
      f"Contact Info: {contact_info}\n"
      f"Number of Floors: {number_of_floors}\n"
      f"Number of Blocks: {number_of_blocks}\n"
      f"Start Block: {start_block}\n"
      f"End Block: {end_block}\n")
        return redirect('society_reg')
    
    else:
        return render(request, 'add_society.html')

def society_reg(request):
    # Retrieve data from session
    user_name = request.session.get('user_name')
    password = request.session.get('password')
    user_type = request.session.get('user_type')
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')
    cnic = request.session.get('cnic')
    phone_number = request.session.get('phone_number')
    address = request.session.get('address')
    society_name = request.session.get('society_name')
    street_address = request.session.get('street_address')
    city = request.session.get('city')
    province = request.session.get('province')
    postal_code = request.session.get('postal_code')
    total_apartments = request.session.get('total_apartments')
    contact_info = request.session.get('contact_info')
    number_of_floors = request.session.get('number_of_floors')
    number_of_blocks = request.session.get('number_of_blocks')
    start_block = request.session.get('start_block')
    end_block = request.session.get('end_block')

    

    # Create User
    user = User(user_name=user_name, password=password, user_type=user_type)
    print("User saved")
    user.save()

    # Create SocietyOwner
    society_owner = SocietyOwner(user_name=user, first_name=first_name, last_name=last_name, phone_number=phone_number, address=address, cnic=cnic)
    print("Owner is going to be saved")
    society_owner.save()
    
    print(f"Society Name: {society_name}\n"
      f"Street Address: {street_address}\n"
      f"City: {city}\n"
      f"Province: {province}\n"
      f"Postal Code: {postal_code}\n"
      f"Total Apartments: {total_apartments}\n"
      f"Contact Info: {contact_info}\n"
      f"Number of Floors: {number_of_floors}\n"
      f"Number of Blocks: {number_of_blocks}\n"
      f"Start Block: {start_block}\n"
      f"End Block: {end_block}\n")

    # Create Society
    society = Society(
        society_name=society_name,
        street_address=street_address,
        city=city,
        province=province,
        postal_code=postal_code,
        total_apartments=total_apartments,
        contact_info=contact_info,
        number_of_floors=number_of_floors,
        number_of_blocks=number_of_blocks,
        start_block=start_block,
        end_block=end_block,
        user_name= user
    )
    society.save()

    # Clear session data
    del request.session['user_name']
    del request.session['password']
    del request.session['user_type']
    del request.session['first_name']
    del request.session['last_name']
    del request.session['phone_number']
    del request.session['address']
    del request.session['society_name']
    del request.session['street_address']
    del request.session['city']
    del request.session['province']
    del request.session['postal_code']
    del request.session['total_apartments']
    del request.session['contact_info']
    del request.session['number_of_floors']
    del request.session['number_of_blocks']
    del request.session['start_block']
    del request.session['end_block']

    return redirect('login')

