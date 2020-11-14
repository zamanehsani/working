from user import views
from django.urls import path, include

from django.contrib.auth import views as auth_views

app_name ='user'
urlpatterns = [
   # path('dashboard/', views.dashboard, name="dashboard"),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="user_login"),
   path('join/', views.join, name="user_join"),
   path('user_profile/', views.user_profile, name="user_profile"),
   path('user_dash/', views.user_dash, name="user_dashboard"),
   path('user_card/', views.user_card_full, name="user_card_full"),
   path('user_profile_edit/', views.user_profile_edit, name="user_profile_edit"),
   path('user_create_card/', views.user_create_card, name="user_create_card"),
]