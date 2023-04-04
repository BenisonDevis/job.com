from django.shortcuts import render

# Create your views here.

def employee_home(request):
    return render(request,'employees_pages/emp_home.html')
    
