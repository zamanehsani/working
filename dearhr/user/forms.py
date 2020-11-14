from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    name    = forms.CharField()
    surname = forms.CharField()
    email   = forms.EmailField()
    class Meta:
        model = User
        fields = ["name","surname","username","email"]