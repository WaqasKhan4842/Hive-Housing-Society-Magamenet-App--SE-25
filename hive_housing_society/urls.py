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
from django.conf import settings

from django.contrib import admin
from django.urls import path
from Home.views import *
from Account.views import *
from vege.views import *
from Resident.views import *
from Building.views import *
from Admin.views import *
from GateKeeper.views import *
from societyforum.views import *
from GateManagement.views import *
from Building.models import Society

urlpatterns = [
    path('', login_view, name='login'),
    path('reg_step1/', reg_step1, name='reg_step1'),  # Removed the trailing comma
    path('reg_step2/', reg_step2, name='reg_step2'),  # Added a trailing slash for consistency
    path('society_reg/', society_reg, name='society_reg'),  # Added a trailing slash for consistency
    path('admin_dashboard/',amdin_dashboard,name="admin_dashboard"),
    path('add_society',add_society,name="add_society"),
    path('apartment_registration/', apartment_registration, name='apartment_registration'),
    path('resident_registration/', resident_registration, name='resident_registration'),
    path('submit_notification/', submit_notification, name='submit_notification'),
    path('gatekeeper_registration/', gatekeeper_registration, name='gatekeeper_registration'),
    path('gatekeeper_dashboard/', gatekeeper_dashboard, name='gatekeeper_dashboard'),
    path('addAmenity/',addAmenity,name="addAmenity"),
    path('display_announcements/', display_announcements,name='display_announcements'),
    path('society_forum/', society_forum,name='society_forum'),
    path('submit_post/', submit_post,name='submit_post'),
    path('submit_comment/<int:post_id>/', submit_comment, name='submit_comment'),
    path('add_emergency_information/', add_emergency_information, name='add_emergency_information'),
    path('display_emergency_information/', display_emergency_information, name='display_emergency_information'),
    path('list_apartments/', list_apartments,name='list_apartments'),
    path('view-dues/<int:apartment_number>/', view_dues, name='view_dues'),
    path('add_dues/<int:apartment_number>/', add_dues, name='add_dues'),
    path('delete_dues/<int:due_id>/', delete_dues, name='delete_dues'),
    path('update-due/<int:due_id>/', update_dues, name='update_dues'),
    path('view_all_dues/', view_all_dues, name='view_all_dues'),

    #path('pay_dues/',pay_dues,name=pay_dues),
    path('get_resident-info/', get_resident_info, name='get_resident_info'),
    path('enter_visitor/', enter_visitor, name='enter_visitor'),
    path('update_exit_time/', update_exit_time, name='update_exit_time'),
    path('lodge_complaint/', lodge_complaint, name='lodge_complaint'),
    path('complaints_list/', complaints_list, name='complaints_list'),
    path('logout_admin/',logout_admin,name='logout_admin'),

    


    




   # path('',Login,name="Login"),
    #path('register/', register_apartment, name='register_apartment'),
    #path('registerresident/', register_resident, name='register_resident'),
    path ('resident_dashboard/',resident_dashboard,name="resident_dashboard"),
    #path('account/', account_view, name='account_view'),
    #path ('',recipes,name="recipes"),
   
    #path('',home,name="home"),
    path('admin/', admin.site.urls),
]

