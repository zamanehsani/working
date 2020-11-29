from django.shortcuts import render, redirect, get_object_or_404
from start.forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, Add_expereince, Add_education, Add_skills, Add_showcase, Add_reference, UserUpdateProfile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from start import models as start_modals
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

def photo(request):
    context = {
        'title': "Photo editing tools"
    }
    return render(request, 'photo.html', context)

def photo_list(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST or None, request.FILES or None)


def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'{username} has been registered!')
            return redirect('login')
    else:
        form = RegisterForm()
    data = {'form': form}
    return render(request, 'registerUser.html', data)

@login_required
def profile(request):
    title = "Profile"
    p_form = ProfileUpdateForm(instance=request.user.user_profile)
    countries = start_modals.Countries.objects.all()
    job_type = start_modals.Job_type.objects.all()
    visa_status = start_modals.Visa.objects.all()
    exp_role_level = start_modals.Experiences_role_level.objects.all()
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.user_profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'profile updated!')
            return redirect('start:user_profile')
        else:
            p_form= ProfileUpdateForm(instance=request.user.user_profile)
            messages.success(request, f'profile not updated!')
            return redirect('start:user_profile')  
    data = {
        'u_form': UserUpdateForm(instance=request.user),
        'up_form': UserUpdateProfile(instance=request.user.user_profile),
        'p_form' : p_form,
        'title': title,
        'visa_status': visa_status,
        'countries': countries,
        'exp_role_level':exp_role_level,
        'job_type':job_type,
        'addShow':Add_showcase(),
        'addSkill':Add_skills(),
        'addEdu':Add_education(),
        'addExp': Add_expereince(),
        'addRef':Add_reference(),
    }
    return render(request, 'user_profile.html', data)

def update(request, id):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserUpdateProfile(request.POST, instance=request.user.user_profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your information has been updated!')
            return redirect('start:user_profile')
        else:
            messages.success(request, p_form.errors)
            return redirect('start:user_profile')
    else:
        messages.success(request, f'data was not sent over post thus has not been saved!')
        u_form = UserUpdateForm( instance=request.user)
        p_form = UserUpdateProfile(instance=request.user.user_profile)
        return redirect('start:user_profile')
   

def addEducation(request):
    if request.method == "GET":
        form = Add_education()
        return redirect('start:user_profile')
    else:
        form = Add_education(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, f'Educations has been added!')
            return redirect('start:user_profile')
        else:
            messages.success(request, form.errors)
            return redirect('start:user_profile')

def addExperience(request):
    if request.method == "GET":
        form = Add_expereince()
        return redirect('start:user_profile')
    else:
        form = Add_expereince(request.POST)
        
        if form.is_valid():
            print(request.POST.get('date_from'))
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, f'Experience has been added!')
            return redirect('start:user_profile')
        else:
            messages.success(request, form.errors)
            return redirect('start:user_profile')

def addReference(request):
    if request.method == "GET":
        form = Add_reference()
        return redirect('start:user_profile')
    else:
        form = Add_reference(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, f'Reference has been added!')
            return redirect('start:user_profile')
        else:
            messages.success(request, form.errors)
            return redirect('start:user_profile')

def addSkill(request):
    if request.method == "GET":
        form = Add_skills()
        return redirect('start:user_profile')
    else:
        form = Add_skills(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, f'Skill has been added!')
            return redirect('start:user_profile')
        else:
            messages.success(request, form.errors)
            return redirect('start:user_profile')

def addShow(request):
    if request.method == "GET":
        form = Add_showcase()
        return redirect('start:user_profile')
    else:
        form = Add_showcase(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, f'Showcase has been added!')
            return redirect('start:user_profile')
        else:
            messages.success(request, form.errors)
            return redirect('start:user_profile')


def delete_skill(request):
    if request.method == 'POST':
        obj = get_object_or_404(start_modals.Skills, id = request.POST.get('id'))
        obj.delete()
        messages.success(request, f'your skill has been removed!')
        return redirect('start:user_profile')


def del_showcase(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        messages.success(request, data)
        return redirect('start:user_profile')
    else:
        messages.success(request, f'something went wrong')
        return redirect('start:user_profile')


def delete_edu(request):
    if request.method == 'POST':
        obj = get_object_or_404(start_modals.Educations, id = request.POST.get('id'))
        obj.delete()
        messages.success(request, f'your Educational record has been removed!')
        return redirect('start:user_profile')

def delete_exp(request):
    if request.method == 'POST':
        obj = get_object_or_404(start_modals.Experiences, id = request.POST.get('id'))
        obj.delete()
        messages.success(request, f'Your Experience record has been removed!')
        return redirect('start:user_profile')

def del_ref(request):
    if request.method == 'POST':
        obj = get_object_or_404(start_modals.References, id = request.POST.get('id'))
        obj.delete()
        messages.success(request, f'your Reference has been delated')
        return redirect('start:user_profile')
@login_required
def user_dash(request):
    title = "Dashboard"
    current_user = request.user
    skill_profile = start_modals.Skills.objects.filter(user_id = current_user.id)
    showcase_profile = start_modals.Showcase.objects.filter(user_id = current_user.id)
    ref_profile = start_modals.References.objects.filter(user_id = current_user.id)

    context = {
        'title': title,
        'skill_profile': skill_profile,
        'showcase_profile' : showcase_profile,
        'ref_profile' : ref_profile,
    }
    return render(request, 'user_dashboard.html', context)

@login_required
def user_create_job(request):
    title = "Create Job Profile"
    context = {
        'title': title, 
    }
    return render(request, 'user_create_card.html', context)

def refview(request):
    if request.method =="GET":
        refid = request.GET['userid']
        ref = start_modals.References.objects.get(id = refid)
        data = [ref.id, ref.title, ref.position, ref.company, ref.description, ref.date, ref.user_id, json.dumps(str(ref.file)) ]
        return JsonResponse(data, safe=False)
    else:
        messages.success(request, f'something went wrong. Plaese try again')
        return redirect('start:user_profile')

        
def updateref(request):
    if request.method =="POST":
        form = Add_reference(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            messages.success(request, f'Your Reference has been updated')
            return redirect('start:user_profile')
        else:
            messages.success(request, form.errors)
            return redirect('start:user_profile')
    else:
        messages.success(request, f'Get request is not processed here!')
        return redirect('start:user_profile')
