from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth.models import User
from .models import UserProfile
#from LibraryProject import settings, User



#@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new UserProfile when a User is created
        UserProfile.objects.create(user=instance)
    else:
        # Save the UserProfile when the User is updated
        instance.userprofile.save()
