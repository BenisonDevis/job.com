from django.shortcuts import render

# Create your views here.


def employee_home(request):
    return render(request, "employees_pages/emp_home.html")


def employee_profile(request):
    return render(request, "employees_pages/emp_profile.html")


def employee_profile_edit(request):
    return render(request, "employees_pages/emp_edit_profile.html")
