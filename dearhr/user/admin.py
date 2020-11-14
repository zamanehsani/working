from django.contrib import admin
from user import models as user_model

admin.site.register(user_model.Education)
admin.site.register(user_model.Company)
admin.site.register(user_model.Address)
admin.site.register(user_model.Location)
admin.site.register(user_model.Skills)
admin.site.register(user_model.Endorsments)
admin.site.register(user_model.References)
admin.site.register(user_model.UserTable)
admin.site.register(user_model.User_account_type)
admin.site.register(user_model.Showcases)
admin.site.register(user_model.Logging)
admin.site.register(user_model.Languages)
admin.site.register(user_model.Visa_type)
admin.site.register(user_model.Jobs)
admin.site.register(user_model.Job_type)
admin.site.register(user_model.Expereince_role_level)
admin.site.register(user_model.Experiences)
admin.site.register(user_model.Tags)
admin.site.register(user_model.Currency)
admin.site.register(user_model.Company_type)


# Register your models here.
