from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, UserExtended

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
   instance.profile.save()

@receiver(post_save, sender=User)
def create_userextended(sender, instance, created, **kwargs):
   if created:
     UserExtended.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userextended(sender, instance, **kwargs):
   instance.userextended.save()