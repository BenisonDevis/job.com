from django.urls import path
from .views import *

urlpatterns = [
    path("employee/home/", employee_home, name="employee_home"),
    path("employee/profile/", employee_profile, name="employee_profile"),
    path("employee/profile/edit", employee_profile_edit, name="employee_profile_edit"),
]
