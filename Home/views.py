from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # when you want to move from one page to the next
    #context = {'Page' : 'home'}
    #return render(request, "home/index.html", context)
    return render(request, "home/index.html")
#return render(request, "index.html", context={'peoples' : people})

# Create your views here.
