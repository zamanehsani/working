from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from start.models import User_profile

class RegisterForm(UserCreationForm):
    first_name  = forms.CharField(max_length=150)
    last_name   = forms.CharField(max_length= 150)
    email       = forms.EmailField()
    class Meta:
        model  = User
        fields = ["first_name","last_name","username","email", "password1","password2"]


class UserUpdateForm(forms.ModelForm):
    email   = forms.EmailField()
    class Meta:
        model  = User
        fields = ["first_name","last_name","username","email"]


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model  = User_profile
        fields = ["phone","mobile","gender","DOB","nationality","image", "marriatal_status", "visa_status"]
    
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['nationality'].empty_label = "Countries"
    
