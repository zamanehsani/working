from django.urls import path, include
from django.contrib.auth import views as auth_views
from start import views as start_views

app_name ="start"
urlpatterns = [
    path('profile/',start_views.profile, name= "user_profile"),
    path('profile/<int:id>', start_views.update, name="profile_update"),
    path("profile/addedu", start_views.addEducation, name= "add_education"),
    path("profile/addExp", start_views.addExperience, name= "add_experience"),
    path("profile/addref", start_views.addReference, name= "add_reference"),
    path("profile/addshow", start_views.addShow, name= "add_showcase"),
    path("profile/addskill", start_views.addSkill, name= "add_skills"),
    path("profile/skill/", start_views.delete_skill, name= "skill_delete"),
    path("profile/edu/", start_views.delete_edu, name= "edu_delete"),
    path("profile/exp/", start_views.delete_exp, name= "exp_delete"),
    path("profile/show", start_views.del_showcase, name= "show_delete"),
    path("dashboard/", start_views.user_dash, name="user_dashboard"),
    path("profile/refview/", start_views.refview, name="refview"),
    path("profile/updateref/", start_views.updateref, name="updateref"),
    path("profile/ref-remove/", start_views.del_ref, name="del_ref"),
    path("createJobProfile/", start_views.user_create_job, name="user_create_job_profile"),
]
