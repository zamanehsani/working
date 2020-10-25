from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name ='dashboard'
urlpatterns = [
    path('index', views.index, name="dashboard_index"),
    # path('profile', views.profile, name="profile"),
    path('register/', views.reg, name="register"),
    path('join/', views.join, name="join"),
    # path("dash/", views.dash, name="user_profile"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout_request, name="logout"),
    path('hrlook/', views.hrlook, name="hrlook"),
]
