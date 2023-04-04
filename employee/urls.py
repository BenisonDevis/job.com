from django.urls import path
from .views import *

urlpatterns = [
    path("", employee_home, name="employee_home"),
]