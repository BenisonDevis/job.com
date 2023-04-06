from django.shortcuts import render,redirect
from .models import *
from account.models import Employee


# Create your views here.


def employee_home(request,):
    return render(request, "employees_pages/emp_home.html")


def employee_profile(request):
    emp = request.user
    
    addskl = AddSkill.objects.filter(
        rel_skill = emp
    )
    addexpe = AddExperience.objects.filter(
        rel_experience = emp
    )
    addeduc = AddEducations.objects.filter(
        rel_education = emp
    )
    addpro = AddProject.objects.filter(
        rel_project = emp
    )
    

    context={
        'emp' : emp,
        'exp' :  addexpe,
        'educ' : addeduc,
        'pro' : addpro,
        'skl' : addskl,
    
    }
    return render(request, "employees_pages/emp_profile.html",context)



def employee_profile_edit(request):
    
    if request.method == 'POST':
        prof_titl=request.POST.get('prof_titl')
        bio=request.POST.get('bio')
        pro_img=request.FILES.get('pro_img')
        pro_cv=request.FILES.get('pro_cv')
        location=request.POST.get('location')
        mob=request.POST.get('mob')
        status=request.POST.get('status')
        gender=request.POST.get('gender')
        
        ProfileEdit.objects.create(
            profile_title = prof_titl,
            bio = bio,
            profile_img = pro_img,
            resume = pro_cv,
            location = location,
            mobile_no = mob,
            working_sts = status,
            gender = gender,
        )
        return redirect('employee_profile')
    return render(request, "employees_pages/emp_edit_profile.html")

def add_experiences(request):
    emp=request.user
    if request.method == 'POST':
        role=request.POST.get('role')
        name=request.POST.get('name')
        year=request.POST.get('year')
        discri=request.POST.get('discri')
        
        AddExperience.objects.create(
            job_role = role,
            date = year,
            company_name = name,
            job_dicription = discri,
            rel_experience = emp
        )
        return redirect('employee_profile')
        
    return render(request, "employees_pages/emp_profile.html")

def add_educations(request):
    emp=request.user
    if request.method == 'POST':
        name=request.POST.get('name')
        quali=request.POST.get('quali')
        year=request.POST.get('year')
        disc=request.POST.get('disc')
        
        AddEducations.objects.create(
            school = name,
            qualification = quali,
            date = year,
            shor_dicription = disc,
            rel_education = emp
        )
        return redirect('employee_profile')
    return render(request, "employees_pages/emp_profile.html")

def add_project(request):
    emp=request.user
    if request.method == 'POST':
        
        name=request.POST.get('name')
        domine=request.POST.get('domine')
        disc=request.POST.get('disc')
        
        AddProject.objects.create(
            pro_name = name,
            domine = domine,
            shor_dicription = disc,
            rel_project = emp
        )
        return redirect('employee_profile')
    return render(request, "employees_pages/emp_profile.html")

def add_skill(request):  
    emp=request.user
    if request.method == 'POST':
        skill=request.POST.get('skill')
        perc=request.POST.get('percentage')
        
        AddSkill.objects.create(
            skill = skill,
            percentage = perc,
            rel_skill = emp
        )
        return redirect('employee_profile',)
        
    return render(request, "employees_pages/emp_profile.html")




