from django.urls import path
from .views import *

urlpatterns = [
    path('company/home/',company_home,name="company_home"),
    path('company/profile/',company_profile,name="company_profile"),
    path('company/profile/edit/',company_profile_edit,name="company_profile_edit"),
    path('company/post/job/',post_job,name="post_job"),
    path('company/job/details/',details_job,name="details_job"),

]