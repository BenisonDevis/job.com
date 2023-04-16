from django.shortcuts import render
from company.models import JobPost

# Create your views here.

def it_field(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    print(post)
    return render(request,'category/it_field.html',context)

def customer_service(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    print(post)
    return render(request,'category/customer_service.html',context)

def human_resource(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    print(post)
    return render(request,'category/human_resource.html',context)

def work_from_home(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    print(post)
    return render(request,'category/work_from_home.html',context)

def mechanical_job(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    print(post)
    return render(request,'category/mechanical_job.html',context)

def automobile(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    print(post)
    return render(request,'category/automobile.html',context)

def education(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    print(post)
    return render(request,'category/education.html',context)

def education(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    print(post)
    return render(request,'category/education.html',context)

def design(request):
    post = JobPost.objects.all()
    context={
        'post' : post
    }
    print(post)
    return render(request,'category/design.html',context)