from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User_account_type(models.Model):
    acount_name = models.CharField(max_length=60, default="Job Seeker")
    Account_type = models.CharField(max_length=10, default="js")
# add all three js, hr, sp to the table

class UserTable(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    user_phone          = models.IntegerField(null=True, blank=True)
    user_mobile         = models.IntegerField(null=True, blank=True)
    user_gender         = models.CharField(max_length=50)
    user_marital_status = models.CharField(max_length=50)
    user_DOB            = models.DateField(null=True, blank=True)
    user_type           = models.ForeignKey(User_account_type, default=1, on_delete=models.DO_NOTHING)
    user_nationality    = models.CharField(max_length=150, null=True, blank=True)
    visa_status         = models.ForeignKey("Visa_type", on_delete= models.DO_NOTHING , default=1)


class Address(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    country         = models.CharField(max_length=150,null=True, blank=True)
    state           = models.CharField(max_length=150,null=True, blank=True)
    city            = models.CharField(max_length=150,null=True, blank=True)
    district        = models.CharField(max_length=150,null=True, blank=True)
    address_line_1  = models.CharField(max_length=150,null=True, blank=True)
    address_line_2  = models.CharField(max_length=150,null=True, blank=True)
    zip_code        = models.SmallIntegerField(null=True, blank=True)
    p_o_box         = models.SmallIntegerField(null=True, blank=True)


class Company(models.Model):
    name        = models.CharField(max_length=200,null=True, blank=True)
    location    = models.ForeignKey("Location", on_delete=models.DO_NOTHING, null=True, blank=True)
    address     = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True)
    website     = models.URLField(null=True, blank=True)
    email       = models.EmailField(null=True, blank=True)
    phone       = models.IntegerField(null=True, blank=True)
    mobile      = models.IntegerField(null=True, blank=True)
    type        = models.ForeignKey("Company_type", on_delete=models.DO_NOTHING,null=True, blank=True)
    logo        = models.ImageField(null=True, blank=True)
    facebook    = models.URLField(null=True, blank=True)
    linkedin    = models.URLField(null=True, blank=True)
    instagram   = models.URLField(null=True, blank=True)
    twitter     = models.URLField(null=True, blank=True)
    youtube     = models.URLField(null=True, blank=True)
    about       = models.TextField(null=True, blank=True)



class Endorsments(models.Model):
    user            = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    user_company    = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True, blank=True)
    user_position   = models.CharField(max_length=200,null=True, blank=True)
    description     = models.TextField(null=True, blank=True)
    date            = models.DateField(null=True, blank=True)

class References(models.Model):
    ref_name        = models.CharField(max_length=200, null=True, blank=True)
    ref_last_name   = models.CharField(max_length=200, null=True, blank=True)
    ref_company     = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True, blank=True)
    ref_position    = models.CharField(max_length=200, null=True, blank=True)
    description     = models.TextField(null=True, blank=True)
    date            = models.DateField(null=True, blank=True)
    ref_file        = models.FileField(null=True, blank=True)
    ref_profile_image = models.ImageField(null=True, blank=True)

class Education(models.Model):
    institute       = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True, blank=True)
    title           = models.CharField(max_length=200, null=True, blank=True)
    date_from       = models.DateField( null=True, blank=True)
    date_to         = models.DateField( null=True, blank=True)
    degree          = models.CharField(max_length=150,null=True, blank=True)
    degree_level    = models.CharField(max_length=200, null=True, blank=True)
    description     = models.TextField( null=True, blank=True)
    logo            = models.ImageField( null=True, blank=True)


class Experiences(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    title           = models.CharField(max_length=200, null=True, blank=True)
    company         = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_from       = models.DateField(null=True, blank=True)
    date_to         = models.DateField(null=True, blank=True)
    type            = models.ForeignKey("Job_type", on_delete=models.DO_NOTHING, null=True, blank=True)
    roles           = models.TextField(null=True, blank=True)
    achievements    = models.TextField(null=True, blank=True)
    descriptions    = models.TextField(null=True, blank=True)
    location        = models.ForeignKey("Location", on_delete=models.DO_NOTHING, null=True, blank=True)
    roles_level     = models.ForeignKey("Expereince_role_level", on_delete=models.DO_NOTHING, null=True, blank=True)


class Location(models.Model):
    country     = models.CharField(max_length=150,null=True, blank=True)
    city        = models.CharField(max_length=150,null=True, blank=True)
    coordinates = models.CharField(max_length=500,null=True, blank=True)


class Company_type(models.Model):
    category    = models.CharField(max_length=200,null=True, blank=True)
    Type        = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True) 


class Currency(models.Model):
    name    = models.CharField(max_length=200,null=True, blank=True)
    code    = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)
    number = models.IntegerField(null=True, blank=True)
    

class Tags(models.Model):
    name = models.CharField(max_length=250,null=True, blank=True)
    date = models.DateField(default=timezone.now)

class Expereince_role_level(models.Model):
    role_name   = models.CharField(max_length=200,null=True, blank=True)
    role_level  = models.SmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Job_type(models.Model):
    job_type_name       = models.CharField(max_length=200)
    type_description    = models.TextField(null=True, blank=True)

class Jobs(models.Model):
    job_name        = models.CharField(max_length=200,null=True, blank=True)
    job_level       = models.SmallIntegerField(null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)


class Visa_type(models.Model):
    visa_name          = models.CharField(max_length=200)
    Visa_category      = models.CharField(max_length=200)
    visa_duration      = models.CharField(max_length=200)
    date_of_issue      = models.DateField(default=timezone.now)
    date_of_expiration = models.DateField(default=timezone.now) 


class Languages(models.Model):
    user                 = models.ForeignKey(User, on_delete=models.CASCADE)
    language_name        = models.CharField(max_length=200, null=True, blank=True)
    level_of_proficiency = models.SmallIntegerField(null=True, blank=True)
    flag                 = models.ImageField(null=True, blank=True)


class Logging(models.Model):
    user        = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    time_in     = models.DateTimeField(null=True, blank=True)
    time_out    = models.DateTimeField(null=True, blank=True)
    ip_address  = models.CharField(max_length=100, null=True, blank=True) 

class Skills(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=200, null=True, blank=True)
    level       = models.SmallIntegerField(default=0, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Showcases(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    path        = models.ImageField(null=True, blank=True)
    title       = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tag         = models.TextField(null=True, blank=True)


