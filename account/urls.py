from django.urls import path
from .views import *

urlpatterns = [
    path("own/account/create/", admin_create, name="admin_create"),
    path("employee/create/", employee_create, name="employee_create"),
    path("company/create/", company_create, name="company_create"),
    path("", user_login, name="user_login"),
    path("user/logout/", user_logout, name="user_logout"),
]
