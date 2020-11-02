from user import views
from django.urls import path

app_name ='user'
urlpatterns = [
   path('dashboard/', views.dashboard, name="dashboard"),
]