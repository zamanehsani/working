from django.shortcuts import render, redirect
from start.forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST,  instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.user_profile)

        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('start:user_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.user_profile)

    data = {
        'u_form': u_form,
        'p_form':p_form,
        'title': title,
    }
    return render(request, 'user_profile.html', data)