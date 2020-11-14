from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from start.models import User_profile

class RegisterForm(UserCreationForm):
    name    = forms.CharField()
    surname = forms.CharField()
    email   = forms.EmailField()
    class Meta:
        model = User
        fields = ["name","surname","username","email"]


class UserUpdateForm(forms.ModelForm):
    email   = forms.EmailField()
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ["image"]