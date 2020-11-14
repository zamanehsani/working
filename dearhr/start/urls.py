from django.urls import path, include
from django.contrib.auth import views as auth_views
from start import views as start_views

app_name ="start"
urlpatterns = [
    path('profile/',start_views.profile, name= "user_profile"),
]
