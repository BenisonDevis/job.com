from django.urls import path
from .views import *

urlpatterns = [
    path("user/create/", company_create, name="company_create"),
    path("user/login/", user_login, name="user_login"),
    path("user/logout/", user_logout, name="user_logout"),
]
