from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# country list
class Countries(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    iso3 = models.CharField(max_length=100, null=True, blank=True)
    iso2 = models.CharField(max_length=100, null=True, blank=True)
    phone_code  = models.CharField(max_length=50, null=True)
    capital     = models.CharField(max_length=150, null=True, blank=True)
    currncy     = models.CharField(max_length=100, null=True, blank=True)
    native      = models.CharField(max_length=150, null=True, blank=True)
    region      = models.CharField(max_length=150, null=True, blank=True)
    subregion   = models.CharField(max_length=150, null=True, blank=True)
    emoji   = models.CharField(max_length=150, null=True, blank=True)
    emojiU   = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name
# states list
class States(models.Model):
    name            = models.CharField(max_length=150, null=True, blank=True)
    country         = models.ForeignKey(Countries, default=1, on_delete=models.CASCADE)
    state_code      = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


#cities
class Cities(models.Model):
    name        = models.CharField(max_length=150, null=True, blank=True)
    country     = models.ForeignKey(Countries, default=1, on_delete=models.CASCADE)
    state       = models.ForeignKey(States, default=1, on_delete=models.CASCADE)
   
    latitude    = models.CharField(max_length=200, null=True, blank=True)
    longitude   = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name



# visa types 
class Visa(models.Model):
    visa_name = models.CharField(max_length=150, null=True, blank=True)
    duration = models.CharField(max_length=150, null=True, blank=True)
    date_of_issue = models.DateField(null=True, blank=True)
    date_of_expire = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.visa_name


# the missing information of user
class User_profile(models.Model):
    u_type = (
        ('Job Seeker', 'Job Seeker'),('HR', 'HR'),('Service Provider', 'Service Provider')
    )
    genders = (
        ('Male', 'Male'),('Female', 'Female'),('Other', 'Other')
    )
    marriatal = (
        ('Signle', 'Single'),('Marriaged', 'Marriaged'),('Devorced', 'Devorced')
    )

    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    gender      = models.CharField(max_length=50, null=True, blank=True, choices=genders)
    DOB         = models.DateField(null=True, blank=True)
    user_type   = models.CharField(max_length=50, null=True, blank=True, choices=u_type)
    mobile      = models.IntegerField(blank=True, null=True)
    phone       = models.IntegerField(blank=True, null=True)
    nationality = models.ForeignKey("countries", null=True, blank=True, on_delete=models.DO_NOTHING)
    marriatal_status   = models.CharField(max_length=50, null=True, blank=True, choices=marriatal)
    image       = models.ImageField(default='default.png', upload_to = "profile_pics")
    visa_status = models.ForeignKey(Visa, on_delete= models.DO_NOTHING) 

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height >300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



# the job type model
class Job_type(models.Model):
    name         = models.CharField(max_length=150, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True) 

    def __str__(self):
        return self.name
    

# # the experiences role model
class Experiences_role_level(models.Model):
    role_level   = models.CharField(max_length=150, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True) 

    def __str__(self):
        return self.role_level



# # the experiences model
# class experiences(models.Model):