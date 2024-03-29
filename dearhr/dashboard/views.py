from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import UserRegisterForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

@login_required
def  index(request):
    return render(request, 'index.html')


def confirm(request):
    return render(request, 'users/page_confirmation.html')

def join(request):
    return render(request, 'join.html')


# this is the registration page. the page that the user is making a user account
def reg(request):
    if request.method == 'POST':
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active = False
            form.save()
            return redirect('dashboard:login')
    else:
        form = UserRegisterForm()
    return render(request, 'user-register.html', {'form': form})

def dash(request):
    return render(request, 'dashboard.html')

def logout_request(request):
    logout(request)
    messages.info(request, "logout successfully")
    return redirect("dashboard:user_profile")

def hrlook(request):
    return render(request, "hrlook.html")

def shortlist(request):
    return render(request, "shortlist.html")

def card(request):
    return render(request, 'detail.html')

def profile(request):
    return render(request, 'profile.html')

def job_post(request):
    return render(request, 'job_post.html')

def testing(request):
    return render(request, 'testing.html')

def profile_edit(request):
    return render(request, 'profile_edit.html')

def analytic_dashboard(request):
    return render(request, 'analytic_dashboard.html')

def job_card(request):
    return render(request, 'analytic_dashboard.html')

def question(request):
    return render(request,'question.html')

def job_post_editor(request):
    return render(request, 'job_post_editor.html')

def create_card(request):
    return render(request, 'create_card.html')

def create_job(request):
    return render(request, 'create_job.html')