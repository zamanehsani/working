from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



def upload_location(instance, filename):
    return "%s/%s" %(instance.id.filename)


class photo(models.Model):
    title = models.CharField(max_length=250, blank=True)
    file = models.ImageField(upload_to = upload_location, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Photo"

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
    emoji    = models.CharField(max_length=150, null=True, blank=True)
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
    visa_name       = models.CharField(max_length=150, null=True, blank=True)
    duration        = models.CharField(max_length=150, null=True, blank=True)
    date_of_issue   = models.DateField(null=True, blank=True)
    date_of_expire  = models.DateField(null=True, blank=True)
    
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
    DOB         = models.DateField("",null=True, blank=True)
    user_type   = models.CharField(max_length=50, null=True, blank=True, choices=u_type)
    mobile      = models.CharField(max_length=150, null=True, blank=True)
    phone       = models.CharField(max_length=150, null=True, blank=True)
    nationality = models.ForeignKey("countries", null=True, blank=True, on_delete=models.DO_NOTHING)
    marriatal_status    = models.CharField(max_length=50, null=True, blank=True, choices=marriatal)
    image               = models.ImageField(default='default.png', upload_to = "profile_pics")
    visa_status         = models.ForeignKey(Visa,null=True, blank=True, on_delete= models.DO_NOTHING) 
    current_location    = models.CharField(max_length=150, null=True, blank=True) 

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        # xcenter = img.width/2
        # ycenter = img.height/2
        # x1 = xcenter - 700
        # x2 = xcenter + 700
        # y1 = ycenter - 700
        # y2 = ycenter + 700
        # cropped = img.crop((x1,y1,x2,y2))
        if img.height >600 or img.width > 600:
            output_size = (600,600)
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
class Experiences(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200, null=True, blank=True)
    company     = models.CharField(max_length=200, null=True, blank=True)
    date_from   = models.DateField( null=True, blank=True)
    date_to     = models.DateField( null=True, blank=True)
    type        = models.ForeignKey(Job_type, on_delete=models.DO_NOTHING, null=True, blank=True)
    roles       = models.TextField(null=True, blank=True)
    achievements= models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location    = models.ForeignKey(Countries, on_delete=models.DO_NOTHING, null=True, blank=True)
    role_level  = models.ForeignKey(Experiences_role_level, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.title

    

# # the education model
class Educations(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200, null=True, blank=True)
    institute   = models.CharField(max_length=200, null=True, blank=True)
    date_from   = models.DateField( null=True, blank=True)
    date_to     = models.DateField( null=True, blank=True)
    degree      = models.CharField(max_length=200, null=True, blank=True)
    degree_level= models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo        = models.ImageField(default='default.png', upload_to = "company_logo")

    def __str__(self):
        return self.title

# # the education model
class Skills(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=200, null=True, blank=True)
    level       = models.PositiveSmallIntegerField(  null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    skill_logo  = models.ImageField(default='skills_logo.png', upload_to = "Skills")

    def __str__(self):
        return self.name

class Showcase(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title       = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image       = models.ImageField(default='showcase.jpg', upload_to = "Showcases")

    def __str__(self):
        return self.title


class References(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    position    = models.CharField(max_length=200, null=True, blank=True)
    company     = models.CharField(max_length=200, null=True, blank=True)
    date        = models.DateField( null=True, blank=True)
    title       = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file        = models.FileField( upload_to = "References", null=True, blank=True)

    def __str__(self):
        return self.title


class Currency(models.Model):
    code    = models.CharField(max_length=20,  null=True, blank=True)
    name    = models.CharField(max_length=150,  null=True, blank=True)
    symbol  = models.CharField(max_length=10,  null=True, blank=True)
    digits  = models.SmallIntegerField( null=True, blank=True)
    number  = models.SmallIntegerField( null=True, blank=True)

    def __str__(self):
        return self.code



# modal for job profile and dashboard
class Js_job_profile(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    title               = models.CharField(max_length=200, null=True, blank=True)
    video               = models.FileField(default='defultvideo.mp4', upload_to = "Job_profile/{User.username}", null=True, blank=True)
    photo               = models.ImageField(default='default.png',   upload_to = "Job_profile/{User.username}",  null=True, blank=True)
    is_activate         = models.BooleanField(default=False,  null=True, blank=True)
    is_complated        = models.BooleanField(default=False, null=True, blank=True)
    is_public           = models.BooleanField(default=True, null=True, blank=True)
    likes               = models.PositiveSmallIntegerField( null=True, blank=True)
    views               = models.PositiveSmallIntegerField( null=True, blank=True)
    shortlist           = models.PositiveSmallIntegerField( null=True, blank=True)
    bio                 = models.TextField( null=True, blank=True)
    targated_location   = models.ForeignKey(Countries, on_delete=models.DO_NOTHING,  null=True, blank=True)
    salary              = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    currency            = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, null=True, blank=True)
    visa_status         = models.ForeignKey(Visa, on_delete=models.DO_NOTHING,  null=True, blank=True )

    def __str__(self):
        return self.title 



class Job_profile_edu(models.Model):
    user        = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    job_profile = models.ForeignKey(Js_job_profile, on_delete=models.CASCADE,  null=True, blank=True)
    education   = models.ForeignKey(Educations, on_delete=models.CASCADE,  null=True, blank=True) 

class Job_profile_exp(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    job_profile     = models.ForeignKey(Js_job_profile, on_delete=models.CASCADE,  null=True, blank=True)
    experience      = models.ForeignKey(Experiences, on_delete=models.CASCADE,  null=True, blank=True) 

    # def __str__(self):
    #     return self.experience 

class Job_profile_show(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    job_profile = models.ForeignKey(Js_job_profile, on_delete=models.CASCADE,  null=True, blank=True)
    showcases   = models.ForeignKey(Showcase, on_delete=models.CASCADE,  null=True, blank=True) 

class Job_profile_skill(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    job_profile = models.ForeignKey(Js_job_profile, on_delete=models.CASCADE,  null=True, blank=True)
    skills      = models.ForeignKey(Skills, on_delete=models.CASCADE,  null=True, blank=True) 

class Job_profile_endors(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    job_profile = models.ForeignKey(Js_job_profile, on_delete=models.CASCADE,  null=True, blank=True)
    endors      = models.ForeignKey(References, on_delete=models.CASCADE,  null=True, blank=True) 






