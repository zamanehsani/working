from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from PIL import Image
from django.conf import settings
from django.core.files import File 
from start.models import User_profile, Experiences, Educations, Skills, Showcase, References




class RegisterForm(UserCreationForm):
    first_name  = forms.CharField(max_length=150)
    last_name   = forms.CharField(max_length= 150)
    email       = forms.EmailField()
    class Meta:
        model  = User
        fields = ["first_name","last_name","username","email", "password1","password2"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ["first_name","last_name","email"]


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model  = User_profile
        fields = ['image']

class UserUpdateProfile(forms.ModelForm):
    DOB = forms.DateField(widget=forms.TextInput(), input_formats=['%d/%m/%Y'])
    class Meta:
        model  = User_profile
        fields = ["gender", "user_type", "mobile","phone","nationality", "marriatal_status", "visa_status", "DOB", "current_location"]



class DateInput(forms.DateInput):
    input_type = 'date'

class Add_expereince(forms.ModelForm):
    date_from = forms.DateField(widget=forms.TextInput(), required=True, input_formats=['%d/%m/%Y'])
    date_to = forms.DateField(widget=forms.TextInput(), required=True, input_formats=['%d/%m/%Y'])
    class Meta:
        model  = Experiences
        fields = ["title","company","date_from","date_to","type", "roles", "achievements","description","location","role_level"]


    def __init__(self, *args, **kwargs):
        super(Add_expereince, self).__init__(*args, **kwargs)
        self.fields['type'].empty_label = ""
        self.fields['role_level'].empty_label = ""
        self.fields['location'].empty_label = ""

class Add_education(forms.ModelForm):
    date_from = forms.DateField(widget=forms.TextInput(), required=True, input_formats=['%d/%m/%Y'])
    date_to = forms.DateField(widget=forms.TextInput(), required=True, input_formats=['%d/%m/%Y'])
    class Meta:
        model  = Educations
        fields = ["title","institute","date_from","date_to", "degree", "degree_level","description","logo"]


class Add_skills(forms.ModelForm):
    level = forms.IntegerField(min_value=0, max_value=100)
    class Meta:
        model  = Skills
        fields = ["name","level","description","skill_logo"]

class Add_showcase(forms.ModelForm):

    class Meta:
        model  = Showcase
        fields = ["title","description","image"]

class Add_reference(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(), required=False, input_formats=['%d/%m/%Y'])
    class Meta:
        model  = References
        fields = ["position","company","date","title","description","file"]
