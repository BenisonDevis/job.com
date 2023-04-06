from django.db import models
from account.models import Employee

# Create your models here.

class AddExperience(models.Model):
    job_role=models.CharField(max_length=50)
    date=models.CharField(max_length=10)
    company_name=models.CharField(max_length=50)
    job_dicription=models.TextField(null=True,blank=True)
    rel_experience=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)

    
    
class AddEducations(models.Model):
    school=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    date=models.CharField(max_length=10)
    shor_dicription=models.TextField(null=True,blank=True)
    rel_education=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
    

class AddProject(models.Model):
    pro_name=models.CharField(max_length=50)
    domine=models.CharField(max_length=50)
    shor_dicription=models.TextField(null=True,blank=True)
    rel_project=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
    
class AddSkill(models.Model):
    skill=models.CharField(max_length=50)
    percentage=models.IntegerField()
    rel_skill=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
    
    
class ProfileEdit(models.Model):
    worksts = (
        ('frsh','I\'m Fresher'),
        ('exp','I\'m Experienced')
    )
    
    gender = (
        ('M','Male'),
        ('F','Female'),
        ('O','Outher')
    )
    
    profile_title = models.CharField(max_length=50)
    bio = models.TextField()
    profile_img = models.ImageField(upload_to='profile.image/',null=True,blank=True)
    resume = models.FileField(upload_to='resume/',null=True,blank=True)
    location = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=12)
    working_sts = models.CharField(max_length=50,choices=worksts)
    gender = models.CharField(max_length=50,choices=gender)