from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver 
from start.models import User_profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        User_profile.objects.create(User = isntance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.User_profile.save()