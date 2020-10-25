from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm


from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# this is the home page after the user is logged in
def home(request):
    return render(request, 'users/home.html')


# this is the confirmation page after the user has registered and is redirected here.
def confirm(request):
    return render(request, 'users/page_confirmation.html')

def join(request):
    return render(request, 'users/join.html')

def password_reset_confirm(request, uidb64, token):
    return render(request, 'users/password_reset_confirm.html')
# this is the registration page. the page that the user is making a user account
def reg(request):
    if request.method == 'POST':
        form= UserRegisterForm (request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active = False
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage( mail_subject, message, to=[to_email] )
            email.send()
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'thanks {last_name}')
            form.save()
            return redirect('users:user_confirm')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!') 


@login_required
def profile(request):
    return render(request, 'users/page_profile.html')

# def logout_view(request):
#     logout(request)












# def sign(request):
#     if request.method == 'POST':
#         form= UserRegisterForm (request.POST)
#         if form.is_valid():
#             save_it = form.save(commit=False)
#             # save_it.save()
#             # send_mail(subject, message, from_email, to_list, fail_silently=True)
#             subject=" thank you for registering"
#             message = "welcome to the DearHR platform./nThis is the activation link"
#             from_email = settings.EMAIL_HOST_USER
#             to_list = [save_it.email]

#             # send_mail(subject, message, from_email , to_list)
#             last_name = form.cleaned_data.get('last_name')
#             messages.success(request, f'thanks {last_name} | {save_it.email}')
#             form.save()
#             return redirect('users:user_confirm')
#         else:
#             return redirect('users:register')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})














    # if request.method == 'POST':
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')        
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     messages.success(request, f'{last_name}')



        # return HttpResponse('<p> done</p>')
        # return redirect ('register')
        # return render(request, 'users/page_confirmation.html')
    # else:
    #     messages.warning(request, f'Account was not created for {last_name}!')
    #     return render( request, 'users/page_confirmation.html')

