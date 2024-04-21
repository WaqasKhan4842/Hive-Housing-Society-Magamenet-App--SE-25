"""
URL configuration for hive_housing_society project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import *
from Account.views import *
from vege.views import *
from Resident.views import *
from Building.views import *
from Admin.views import *

urlpatterns = [
    path('',Admin_Dashboard,name="Admin_Dashboard"),
    #path('',add_society,name="add_society"),
    #path('',Add_Amenity,name="Add_Amenity"),
   # path('',Login,name="Login"),
    path('registerresident/', register_resident, name='register_resident'),
   #path ('Resident_Dashboard/',Resident_Dasboard,name="Resident_Dasboard"),
    path('account/', account_view, name='account_view'),
    #path ('',recipes,name="recipes"),
   
    #path('',home,name="home"),
    path('admin/', admin.site.urls),
]
