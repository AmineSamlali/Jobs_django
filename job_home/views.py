from django.shortcuts import render ,get_object_or_404 , redirect
from .models import Added_JOBS , CEVEE 
from django.core.paginator import Paginator
from .forms import Form_cv , Form_addjobs , Form_auto
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError



@login_required
def post_ajob(request):
    pop =  Form_addjobs

    if request.method == 'POST':
        myform = Form_addjobs(request.POST ,request.FILES)
        if myform.is_valid():
            forma = myform.save(commit=False)
            forma.auther = request.user
            forma.save()
    
            return redirect('test')
    


    context= {'Form':pop}
    return render(request , 'POST_JOB.html' ,context)




def post_id(request , slug):
    kwili = get_object_or_404(Added_JOBS , slug=slug)
    Form = Form_cv()
    form_auth = Form_auto()
    user_login = request.user
    if user_login != kwili.auther:
        if request.method == "POST":
            Form = Form_cv(request.POST,request.FILES)
            form_auth = Form_auto(request.POST,request.FILES)
            if Form.is_valid():
                myform = Form.save(commit=False)
                myform.job_Name = kwili
                myform.save()
            elif form_auth.is_valid():
                print('#'*100)
                myForm = form_auth.save(commit=False)
                myForm.job_Name = kwili
                myForm.name = request.user
                myForm.Email = request.user.email
                myForm.save()
                print('#'*100)
        else:
            form_auth = Form_auto()
            Form = Form_cv()
        context = {
            'obj': get_object_or_404(Added_JOBS , slug=slug),
            'Form':Form,
            'form_auth':form_auth

        }
    else:
        context={
            'obji': get_object_or_404(Added_JOBS , slug=slug),


        }
    return render (request  , 'job_details.html' ,context )





def test_project(request):
    count_jobs = Added_JOBS.objects.count()
    k = 1
    count_jobs_1 = count_jobs - k
    pagges = Added_JOBS.objects.all()


    paginator = Paginator(pagges, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'count_job': count_jobs_1 ,
        'jobs': page_obj,
    } 


    return render ( request , 'index.html' , context)










