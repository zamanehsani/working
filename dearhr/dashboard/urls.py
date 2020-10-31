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
    path('shortlist/', views.shortlist, name="shortlist"),
    path('card/', views.card, name="card"),
    path('general_info/', views.general_info, name="general_info"),
    path('job_post/', views.job_post, name="hr_dashboard"),
    # path('testing/', views.testing, name="testing"),
    path('profile_edit/', views.profile_edit, name="profile_edit"),
    path('analytic_dashboard/', views.analytic_dashboard, name="analytic_dashboard"),
    path('job_card/', views.job_card, name="job_card"),
    path('question/', views.question, name="question"),
    path('job_post_editor/', views.job_post_editor, name="job_post_editor"),
    path('create_card/', views.create_card, name="create_card"),
]
