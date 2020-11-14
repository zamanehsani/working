from django.shortcuts import render, redirect
from  user.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from user import models
from django.contrib.auth.models import User

def join(request):
    if request.method == 'POST':
        form = RegisterForm (request.POST)
        if form.is_valid():
            user.is_active = True
            form.save()
            return redirect('user:user_login')
    else:
        form = RegisterForm()
    return render(request, 'join.html', {'form': form})




# your profile
@login_required
def user_profile(request):
    page_title = "Profile"
    obj = models.UserTable.objects.get(id=2)
    userobj = User.objects.get(id=6)
    context ={ "title":page_title, "obj":obj, "userobj": userobj,}
    return render(request, 'user_profile.html', context)




# user dashboard
@login_required
def user_dash(request):
    page_title = "Dashboard"
    obj = UserTable.objects.get(id=2)

    context ={ "title":page_title, "obj":obj}

    return render(request, 'user_dashboard.html', context)


def user_card_full(request):
    return render(request, 'user_card_full.html')

def user_profile_edit(request):
    return render(request, 'user_profile_edit.html')

def user_create_card(request):
    return render(request, 'user_create_card.html')



