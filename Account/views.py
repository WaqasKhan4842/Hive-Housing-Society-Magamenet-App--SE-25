from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import User



def Login(request):
    error_message = None
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        print(user_name)
        print(password)
        
        # Authenticate user
        user = authenticate(request, username=user_name, password=password)
        
        if user is not None:
            # User is authenticated, login user
            login(request, user)
            return render(request, "home/Login.html", {'error_message': error_message}) # Redirect to the dashboard upon successful login
        else:
            # Authentication failed, show error message
            error_message = "Invalid username or password. Please try again."
            print("Invalid username or password. Please try again.")
            return redirect('Resident_Dashboard/')
            
        
    return render(request, "home/Login.html")




    # when you want to move from one page to the next
    #context = {'Page' : 'home'}
    #return render(request, "home/index.html", context)
   
#return render(request, "index.html", context={'peoples' : people})

# Create your views here.
