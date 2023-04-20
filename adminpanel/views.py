from django.shortcuts import render,redirect
from account.models import Employee,Company
from company.models import CompanyProfile
from employee.models import ProfileEdit
# Create your views here.

def admin_homepage(request):
    emp = Employee.employee.all()
    emplen=len(emp)
    comp = Company.company.all()
    complen = len(comp)
    context = {
        'emplen' : emplen,
        'complen' : complen
    }
    return render(request,'admin/admin_home.html',context)


def admin_employees_details(request):
    emp = Employee.employee.all()
    
    emp_prof = ProfileEdit.objects.filter(
        rel_profile__in = emp.values_list('id',flat=True)
    )
    context = {
        'emp' : emp,
        'emp_prof' : emp_prof
    }
    return render(request,'admin/admin_employess.html',context)


def admin_companies_details(request):
    comp = Company.company.all()
    
    comp_prof = CompanyProfile.objects.filter(
    rel_comp__in = comp.values_list('id', flat=True)
)
    print(comp_prof)
    context = {
        'comp' : comp,
        'comp_prof' : comp_prof
    }
    return render(request,'admin/admin_companies.html',context)


def delete_account_company(request,id):
    comp = Company.company.get(id=id)
    comp.delete()
    return redirect('admin_companies_details')


def delete_account_employee(request,id):
    emp = Employee.employee.get(id=id)
    emp.delete()
    return redirect('admin_employees_details')

def login_permissions(request):
    comp = Company.company.all()
    
    context = {
        'comp' : comp
    }
    
    return render(request,'admin/login_permission.html',context)
    
def permission_done(request,id):
    comp = Company.objects.get(id=id)

    print('hello')
    if request.method == 'POST':
        permision = request.POST.get('select')
        
        if permision == 'on':
            print(comp)
            comp.is_active = True
            comp.save()
            return redirect('login_permissions')
        else:
            print(False)
            comp.is_active = False
            comp.save()
            return redirect('login_permissions')
    context={
        'comp' : comp
    }
    return render(request,'admin/login_permission.html', context)

def approve_sts(request,id):
    comp = Company.objects.get(id=id)
    print(comp.id)
    comp.is_active = not comp.is_active
    comp.save()
    return redirect('login_permissions')