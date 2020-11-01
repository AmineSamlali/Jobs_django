from django.shortcuts import redirect, render ,get_object_or_404
from .forms import signUP , UserForm , ProfileForm 
from django.contrib.auth import authenticate, login
from .models import Profile 
from django.contrib.auth.decorators import login_required
from job_home.models import Added_JOBS
from job_home.forms import Form_addjobs
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    form = signUP
    if request.method == 'POST':
        form = signUP(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('test')
            

    else:
        form = signUP

    context = {
        'form':form

    }
    return render(request , 'registration/signUP.html',context) 







@login_required
def dash_edit(request,slug):
    formula = Added_JOBS.objects.get(slug=slug)
    if formula.auther == request.user:
        if request.method == "POST":
            Form =  Form_addjobs(request.POST,request.FILES,instance=formula)
            if Form.is_valid():
                mayform = Form.save()
                return  redirect('dash')
        else:
            Form =  Form_addjobs(instance=formula)
        context =  {
            'Form':Form
        }
    else:
        print("%"*1000)
        context =  {
            '':''
        }

    return render(request , 'profile/dash_edit.html',context)



@login_required
def dash(request):
    user_filter = Added_JOBS.objects.filter(auther=request.user)
    user_count = user_filter.count()
    context = {

       'jobs' : user_filter,
       'counts':user_count
    }
    return render(request , 'profile/dash.html',context)















@login_required
def profile_edit(request):
    profilee = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profile_show = UserForm(request.POST,instance=request.user)
        profile_edit = ProfileForm(request.POST,request.FILES,instance=profilee)
        if profile_show.is_valid() and profile_edit.is_valid():
            profile_show.save()
            mayForm = profile_edit.save(commit=False)
            mayForm.user = request.user
            mayForm.save()
            return redirect('profile_user')
    else:
        profile_edit = ProfileForm(instance=profilee)
        profile_show = UserForm(instance=request.user)


        
    context = {
        'UserForm':profile_show,
        'ProfileForm':profile_edit,


    }
    return render(request ,'profile/profile_edit.html', context)
@login_required
def profile_shower(request):
    profile_user = Profile.objects.get(user=request.user)
    return render( request , 'profile/profile.html', {'profile_id':profile_user} )








