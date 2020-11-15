from django.contrib import admin
from . import models  

admin.site.register(models.User_profile)
admin.site.register(models.Countries)
admin.site.register(models.States)
admin.site.register(models.Cities)
admin.site.register(models.Visa)
admin.site.register(models.Job_type)
admin.site.register(models.Experiences_role_level)