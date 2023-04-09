from django.shortcuts import render,redirect
from .models import CompanyProfile,JobPost
from account.models import Company

# Create your views here.

def company_home(request):
    comp = request.user
    edit_pro = CompanyProfile.objects.filter(
        rel_comp = comp
    )
    post = JobPost.objects.filter(
        rel_comp_job = comp
    )
    
    context = {
        'comp' : comp,
        'edit_pro' : edit_pro,
        'post' : post
    }
    
    return render(request,'company/company_home.html',context)


def company_profile(request):
    comp = request.user
    edit_pro = CompanyProfile.objects.filter(
        rel_comp = comp
    ).first()
    context = {
        'comp' : comp,
        'edit_pro' : edit_pro
    }
    return render(request,'company/company_profile.html',context)

def company_profile_edit(request):
    comp = request.user
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        slogan = request.POST.get('slogan')
        company_logo = request.FILES.get('company_logo')
        cover_image = request.FILES.get('cover_image')
        about_disc = request.POST.get('about_disc')
        about_img = request.FILES.get('about_img')
        outh_title = request.POST.get('outh_title')
        outh_disc = request.POST.get('outh_disc')
        outh_img = request.FILES.get('outh_img')
        location = request.POST.get('location')
        
        CompanyProfile.objects.create(
            company_name = company_name,
            company_logo = company_logo,
            company_prf_bg = cover_image,
            company_slogam = slogan,
            company_location = location,
            about_us_img = about_img,
            about_us_discpt = about_disc,
            outher_det_title = outh_title,
            outher_det_image = outh_img,
            outher_det_discription = outh_disc,
            rel_comp = comp            
        )
        return redirect('company_profile')
    return render(request,'company/company_profile_edit.html')


def post_job(request):
    user = request.user
    if request.method == 'POST':
        jobtitle = request.POST.get('jobtitle')
        location = request.POST.get('location')
        lastdate = request.POST.get('lastdate')
        jobtype = request.POST.get('jobtype')
        vacancy = request.POST.get('vacancy')
        price = request.POST.get('price')
        job_discription = request.POST.get('job_discription')
        short_discription = request.POST.get('short_discription')
        required = request.POST.get('required')
        education = request.POST.get('education')
        status = request.POST.get('status')
        if status:
            JobPost.objects.create(
                jobtitle = jobtitle,
                location = location,
                jobtype = jobtype,
                last_date = lastdate,
                vacancy = vacancy,
                price_range = price,
                job_discription = job_discription,
                short_discription = short_discription,
                required = required,
                education = education,
                status = True,
                rel_comp_job = user
            )
            print('hello')
            return redirect('company_home')
        else:
            JobPost.objects.create(
                jobtitle = jobtitle,
                location = location,
                jobtype = jobtype,
                last_date = lastdate,
                vacancy = vacancy,
                price_range = price,
                job_discription = job_discription,
                short_discription = short_discription,
                required = required,
                education = education,
                status = False,
                rel_comp_job = user
            )
            print('hai')
            return redirect('company_home')
        
    return render(request,'company/job_post.html')


def details_job(request):
    return render(request,'company/job-detail.html')
    