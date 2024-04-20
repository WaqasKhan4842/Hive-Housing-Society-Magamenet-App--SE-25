from django.shortcuts import render
from django.http import HttpResponse


def Resident_Dasboard(request):
    return render(request,'dashboard.html')



def account_view(request):
    return render(request,'account_view.html')





# Create your views here.
