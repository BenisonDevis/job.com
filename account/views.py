from django.shortcuts import render, redirect
from .models import Account, Employee, Company
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, "base.html")


def admin_create(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("firstname")
        email = request.POST.get("email")
        role = request.POST.get("role")
        pasw1 = request.POST.get("password1")
        pasw2 = request.POST.get("password2")

        user = Account.objects.filter(username=username)
        if not user:
            if pasw1 == pasw2:
                Account.objects.create_user(
                    username=username,
                    first_name=fname,
                    role=role,
                    email=email,
                    password=pasw1,
                )
                messages.success(request, "Account create Successfuly")
                return redirect("user_login")
            else:
                messages.error(request, "Password does not match")
        else:
            messages.error(request, "Username already exits ")

    return render(request, "accounts/create_user.html")


def employee_create(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        email = request.POST.get("email")
        # role = request.POST.get("role")
        pasw1 = request.POST.get("password1")
        pasw2 = request.POST.get("password2")

        user = Employee.objects.filter(username=username)
        if not user:
            if pasw1 == pasw2:
                Employee.objects.create_user(
                    username=username,
                    first_name=fname,
                    last_name=lname,
                    email=email,
                    password=pasw1,
                    is_active =True
                )
                messages.success(request, "Account create Successfuly")
                return redirect("user_login")
            else:
                messages.error(request, "Password does not match")
        else:
            messages.error(request, "Username already exits ")

    return render(request, "accounts/create_user.html")


def company_create(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("firstname")
        email = request.POST.get("email")
        role = request.POST.get("role")
        pasw1 = request.POST.get("password1")
        pasw2 = request.POST.get("password2")

        user = Company.objects.filter(username=username)
        if not user:
            if pasw1 == pasw2:
                Company.objects.create_user(
                    username=username,
                    first_name=fname,
                    role=role,
                    email=email,
                    password=pasw1,
                )
                messages.success(request, "Account create Successfuly")
                return redirect("user_login")
            else:
                messages.error(request, "Password does not match")
        else:
            messages.error(request, "Username already exits ")

    return render(request, "accounts/create_user.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, "Login")
            if request.user.role == "USER":
                return redirect("employee_home")
            elif request.user.role == "COMPANY":               
                return redirect("company_home")
            elif request.user.role == "ADMIN":
                return redirect("admin_homepage")
        else:
            messages.error(request, "invalid username or password")

    return render(request, "accounts/login_user.html")


def user_logout(request):
    logout(request)
    return redirect(
        "user_login",
    )
